# -*- coding: utf-8 -*-

import json
import requests
from flask import request

from Project import *


from zalo.sdk.oa import ZaloOaInfo, ZaloOaClient

zalo_info = ZaloOaInfo(oa_id=app.config['ZALO_OA_ID'], secret_key=app.config['ZALO_PAGE_ACCESS_TOKEN'])
zalo_oa_client = ZaloOaClient(zalo_info)


@app.route('/zalo', methods=['GET'])
def zalo_verify():
    data = request.args
    mess = data.get('message')

    print('Zalo req mess: ' + mess)
    rs = Predict(mess)
    userID = data.get('fromuid')
    returnMessage = rs
    data = {
        'uid': userID,
        'message': returnMessage
    }
    params = {'data': data}
    send_text_message = zalo_oa_client.post('sendmessage/text', params)

    return "Hello world", 200
