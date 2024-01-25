import regex as re
from pyvi import ViTokenizer

def remove_punc(text):
        text = text.lower()
        text = re.sub(r'[^\w\d\sàáãạảăắằẳẵặâấầẩẫậèéẹẻẽêềếểễệđìíĩỉịòóõọỏôốồổỗộơớờởỡợùúũụủưứừửữựỳỵỷỹýÀÁÃẠẢĂẮẰẲẴẶÂẤẦẨẪẬÈÉẸẺẼÊỀẾỂỄỆĐÌÍĨỈỊÒÓÕỌỎÔỐỒỔỖỘƠỚỜỞỠỢÙÚŨỤỦƯỨỪỬỮỰỲỴỶỸÝ]|\_', ' ', text)
        text = re.sub(r'\s+', ' ', text)
        
        return text.strip()


def preprocess_sa(text):
    text = remove_punc(text)
    text = ViTokenizer.tokenize(text)

    return text

def preprocess_ner(text):
    text = remove_punc(text)
    return text
