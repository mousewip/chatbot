# -*- coding: utf-8 -*-
__version__ = '1.0'
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os, random
from src.text_classification_predict import TextClassificationPredict

app = Flask('Project', template_folder='Views')
app.config['SECRET_KEY'] = 'mousewip-bot'
app.config['SESSION_TYPE'] = 'filesystem'
app.config.from_pyfile('config.cfg')
app.debug = True


APP_ROOT = os.path.dirname(__file__)
UPLOAD_PATH = os.path.join(APP_ROOT, 'static/uploads')


db = SQLAlchemy(app)


def Serializable(form):
    _input_dict = {}
    for key, value in list(form.items()):
        _input_dict[key] = value
    return _input_dict


tcp = TextClassificationPredict()
model = tcp.get_model()


def Predict(pred_src):
    global tcp
    rs, accu = tcp.predict_conv(pred_src)

    if rs == "mo_ta_trieu_chung":
        rs = tcp.predict(pred_src)
        return rs
    else:
        # chao_hoi, tro_giup, ket_thuc
        if rs == "chao_hoi":
            lst_rs = []
            lst_rs.append("Xin chào bạn, bạn cần trợ giúp gì?")
            lst_rs.append("Xin chào bạn, bạn cần hỗ trợ gì?")
            lst_rs.append("Bot có thể giúp gì cho bạn?")
            lst_rs.append("Supper Bot Y tế có mặt. Bạn cần gì nè?")
            rs = random.choice(lst_rs)

        elif rs == "ket_thuc":
            rs = "Cám ơn bạn đã sử dụng dịch vụ."
        elif rs == "tro_giup" and accu >= 0.5:
            rs = "Bạn cần hỗ trợ gì?"
        else:
            rs = "Xin lỗi, bạn vui lòng hỏi câu khác nhé!"
    return rs


from Project.Controllers import *
