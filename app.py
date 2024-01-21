from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/predict', methods=['GET'])
def predict():
    try:
        # Gọi mô hình   
        # prediction = predict_function()

        #sample data
        sample_data = [
        {"text": "Sp ổn, mỗi tội vân tay lúc nhận lúc không, nhân viên nhiệt tình, pin trâu, cả đêm tụt 1%",
         "labels": [[0, 5, "GENERAL#POSITIVE"], [15, 41, "FEATURES#NEGATIVE"], [43, 63, "SER&ACC#POSITIVE"], [65, 88, "BATTERY#POSITIVE"]]},
        {"text": "Mua cho mẹ sài nên củng không đòi hỏi gì nhiều, máy đẹp camera siêu ảo, thử chiến game củng ok,pin sài dc 2 ngày với luot wep xem fim, nhân viên tgdd an minh KG phục vụ qua nhiệt tình cho 5*",
         "labels": [[48, 55, "DESIGN#POSITIVE"], [55, 70, "CAMERA#POSITIVE"], [72, 94, "PERFORMANCE#POSITIVE"], [95, 133, "BATTERY#POSITIVE"], [135, 183, "SER&ACC#POSITIVE"]]},
        {"text": "Sản phẩm qua tệ sai mấy lời liên tục sắc không võ cử sắc thì sắc không được .đem sắc mấy khác thì lại vô bin.còn đem về đung mài sắc không .lâu lâu mấy sắc không .tật mây khói đông lại thì sắc vô.đem lên thế giới gỉ đồng thì kêu đem lên hàng bạo hành .mình đó toàn diện mấy xanh với thời giới gỉ đồng .mã lực này bạo hành mấy của tg đồng kẻm làm .mình không ủng hộ nữa đâu",
         "labels": [[0, 15, "GENERAL#NEGATIVE"], [37, 138, "BATTERY#NEGATIVE"], [196, 372, "SER&ACC#NEGATIVE"]]},
        {"text": "Mình mua máy hôm 3/5 ở TGDĐ Nguyễn Thị Tú. Nhân viên tư vấn nhiệt tình, khs ok. Cảm nhận của mình về máy khá mượt, cam đẹp, pin khá ổn mình sử dụng chơi game (LQMB,PUBG,...) và lướt mxh khá nhiều nhưng tới cuối ngày pin vẫn còn hơn 30%. Nói chung là máy khá tôt, ổn trong tầm giá, tuy nhiên lâu lâu có hơi khựng 1 chút nhưng tần suất không nhiều. Ý kiến của riêng mình cảm ơn mn",
         "labels": [[43, 78, "SER&ACC#POSITIVE"], [80, 113, "PERFORMANCE#POSITIVE"], [115, 122, "CAMERA#POSITIVE"], [124, 235, "BATTERY#POSITIVE"], [237, 265, "GENERAL#POSITIVE"], [291, 345, "PERFORMANCE#NEUTRAL"]]},
        {"text": "Máy xài tốt, mượt, sạc rất nhanh, pin trâu, mình dùng tác vụ bình thường (zalo, fb, youtube) thì được 1 ngày rưỡi. Camera thì đẹp ảo 😁.",
         "labels": [[0, 11, "GENERAL#POSITIVE"], [13, 17, "PERFORMANCE#POSITIVE"], [19, 32, "BATTERY#POSITIVE"], [34, 42, "BATTERY#POSITIVE"], [115, 132, "CAMERA#POSITIVE"]]},
        {"text": "Mình mới mua. mình thấy mẫu đẹp pin trâu cảm ứng mượt được em nhân viên ĐMX tư vấn rất nhiệt tình",
         "labels": [[19, 31, "DESIGN#POSITIVE"], [32, 40, "BATTERY#POSITIVE"], [41, 53, "FEATURES#POSITIVE"], [54, 97, "SER&ACC#POSITIVE"]]},
        {"text": "Máy Sài rất êm mượt mà còn thắc mắc iphone7 plus có chống nước ko bị rơi xuống nước 1 lần rồi và ko sao cả",
         "labels": [[0, 22, "PERFORMANCE#POSITIVE"]]}
        ]
        
        response = sample_data

        return jsonify(response)
    except Exception as e:
        return jsonify({"error": str(e)})

if __name__ == '__main__':
    app.run(debug=True)
