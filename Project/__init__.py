# -*- coding: utf-8 -*-
__version__ = '1.0'
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os, random, datetime
from src.text_classification_predict import TextClassificationPredict
from src.remove_accent_vietnamese import no_accent_vietnamese_unicode


app = Flask('Project', template_folder='Views')
app.config['SECRET_KEY'] = 'mousewip-bot'
app.config['SESSION_TYPE'] = 'filesystem'
app.config.from_pyfile('config.cfg')
app.debug = True

APP_ROOT = os.path.dirname(__file__)
UPLOAD_PATH = os.path.join(APP_ROOT, 'static/uploads')

db = SQLAlchemy(app)

from Project.Models import MWModel
def Serializable(form):
    _input_dict = {}
    for key, value in list(form.items()):
        _input_dict[key] = value
    return _input_dict


tcp = TextClassificationPredict()
model = tcp.get_model()


def Predict(pred_src, chanel):
    global tcp
    pred_text = pred_src.replace('\n', ' ').strip().lower()
    rs, accu = tcp.predict_conv(pred_text)
    pre = rs
    print('accu {accu}'.format(accu=accu))

    if rs == "mo_ta_trieu_chung" and accu >= 50:
        rs, accu = tcp.predict(pred_text)
        pre = no_accent_vietnamese_unicode(rs).replace(' ', '_')
        cq = MWModel.ClientQuery(
            q_date=datetime.date.today(),
            q_time=datetime.datetime.now(),
            request=pred_text,
            answer=rs,
            predicted=pre,
            accuracy=accu,
            chanel=chanel,
            status='success',
            pre_type='predict',
            solve='',
            from_u=''
        )
        cq = MWModel.add(cq)
        return "Có thể bạn đang bị {rs}".format(rs=rs)
    elif rs == "mo_ta_trieu_chung" and accu < 50:
        rs = "Xin lỗi, bạn vui lòng hỏi câu khác nhé!"
        pre = 'unknown'
    else:
        # chao_hoi, tro_giup, ket_thuc
        if rs == "chao_hoi":
            rs = "Chào mừng bạn đến với chúng tôi!\nTôi là Chatbot hỗ trợ chuẩn đoán các bệnh thường gặp ở người.\nVui lòng mô tả triệu chứng bệnh của bạn ở ô chat."

        elif rs == "ket_thuc":
            rs = "Cám ơn bạn đã sử dụng dịch vụ."
        elif rs == "tro_giup" and accu >= 50:
            rs = "Bạn cần hỗ trợ gì?"
        else:
            pre = 'unknown'
            rs = "Xin lỗi, bạn vui lòng hỏi câu khác nhé!"

    cq = MWModel.ClientQuery(
        q_date=datetime.date.today(),
        q_time=datetime.datetime.now(),
        request=pred_text,
        answer=rs,
        predicted=pre,
        accuracy=accu,
        chanel=chanel,
        status='success',
        pre_type='conversation',
        solve='',
        from_u=''
    )
    cq = MWModel.add(cq)
    return rs


from Project.Controllers import *
