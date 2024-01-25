import findspark
findspark.init()

import pyspark
from pyspark.sql import SparkSession
from time import sleep
from pyspark import SparkContext, SparkConf

scala_version = '2.12'  # your scala version
spark_version = '3.5.0' # your spark version
kafka_version = '2.5.0' # your kafka version

packages = [
    f'org.apache.spark:spark-sql-kafka-0-10_{scala_version}:{spark_version}',
    f'org.apache.kafka:kafka-clients:{kafka_version}' 
]

spark = SparkSession.builder \
                    .master("local")\
                    .appName("kafka-shopee")\
                    .config("spark.jars.packages", ",".join(packages))\
                    .config("spark.executor.memory", "16g") \
                    .config("spark.driver.memory", "16g") \
                    .config("spark.python.worker.reuse",True) \
                    .config("spark.sql.execution.arrow.maxRecordsPerBatch", "16") \
                    .getOrCreate()


spark.conf.set("spark.sql.adaptive.enabled", "false")
spark.conf.set("spark.sql.streaming.forceDeleteTempCheckpointLocation", "true")

print(packages)

topic_name = 'ryhjlimi-shopee'
kafka_server = 'dory-01.srvs.cloudkafka.com:9094'

from pyspark.sql.types import StructType, StructField, StringType, IntegerType

streamRawDf = spark\
                .readStream\
                .format("kafka")\
                .option("kafka.bootstrap.servers", kafka_server)\
                .option("subscribe", topic_name)\
                .option("startingOffsets", "latest")\
                .option("kafka.security.protocol", "SASL_SSL")\
                .option("kafka.sasl.mechanism", "SCRAM-SHA-256")\
                .option("kafka.sasl.jaas.config", "org.apache.kafka.common.security.scram.ScramLoginModule required username=\"ryhjlimi\" password=\"LuUoqLhDxrLrFDGjJPDxoaW1i4lnKaOl\";")\
                .option("failOnDataLoss", "false") \
                .load()

from pyspark.sql.functions import col, udf, from_json

# Define the JSON schema
json_schema = StructType([
    StructField("cmtid", StringType(), True),
    StructField("comment", StringType(), True),
    StructField("rating_star", IntegerType(), True),
])

streamDF = streamRawDf \
    .selectExpr("CAST(value AS STRING)") \
    .select(from_json("value", json_schema).alias("data")) \
    .select("data.*")

from preprocess import preprocess_ner, preprocess_sa
from pyspark.sql.functions import udf

sa = udf(preprocess_sa, StringType())
ner = udf(preprocess_ner, StringType())

cleanDF = streamDF\
    .withColumn("sa_cmt", sa(col('comment')))\
    .withColumn("ner_cmt", ner(col('comment')))\

import requests

# Define a function to send individual records to the localhost server
def send_record_to_server(record):
    url = "http://localhost:5000"
    response = requests.post(url, json=record.asDict())

output_path = "D:/UIT/Visual-Dashboard-IE212-/preprocessed/data"
checkpoint_location = "D:/UIT/Visual-Dashboard-IE212-/preprocessed/checkpoint"

stream_writer = (
    cleanDF\
    .writeStream 
    .queryName("cleanComments") 
    .outputMode("append")
    .format("csv")
    .option("path", output_path) 
    .option("checkpointLocation", checkpoint_location) 
    .option("truncate", False)
    .option("header", True)
    .foreach(send_record_to_server)
    .trigger(processingTime="10 seconds") 
)

query_hdfs = stream_writer.start()
query_hdfs.awaitTermination()