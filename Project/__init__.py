# -*- coding: utf-8 -*-
__version__ = '1.0'
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os
from sklearn.externals import joblib
import pandas as pd

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


def LoadModel():
    model = joblib.load(APP_ROOT + '/MLModel/model.sav')
    print('Load Model Success')
    return model

model = LoadModel()

def Predict(pred_src):
    test_data = []
    test_data.append({"feature": pred_src, "target": ""})
    df_test = pd.DataFrame(test_data)
    predicted = model.predict(df_test["feature"])

    # Print predicted result
    print(predicted)
    result = predicted[0]
    proba = model.predict_proba(df_test["feature"])
    accu = max(proba[0])
    return 'Có thể bạn đang bị: {res}\nĐộ tin cậy: {per}%'.format(res=result, per=accu*100)

from Project.Controllers import *
