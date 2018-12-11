# -*- coding: utf-8 -*-
__version__ = '1.0'
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os
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

    if rs == "tro_giup" and accu <= 0.5:
        rs = tcp.predict(pred_src)
    print(rs)
    return rs


from Project.Controllers import *
