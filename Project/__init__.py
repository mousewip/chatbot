# -*- coding: utf-8 -*-
__version__ = '1.0'
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os

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


from Project.Controllers import *
