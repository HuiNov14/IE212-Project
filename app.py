from flask import Flask, render_template, request
from flask_cors import CORS
from predict import absa

app = Flask(__name__)
CORS(app)

data = []

@app.route('/predict', methods=['GET'])
def predict():
    return data

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        req = request.json
        
        data.insert(
            0,
            absa(
                req['comment'],
                req['ner_cmt'],
                req['sa_cmt'],
            )
        )
    
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
