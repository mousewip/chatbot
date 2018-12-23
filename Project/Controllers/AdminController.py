# -*- coding: utf-8 -*-

from flask import render_template, jsonify, request

from Project import *
from Project.Models import *
import datetime, json


@app.route('/admin')
def Admin():
    d = datetime.datetime.today().date()

    c_web = MWModel.countByChanelInDay('Web', d)
    c_zalo = MWModel.countByChanelInDay('Zalo', d)
    c_fb = MWModel.countByChanelInDay('FB', d)
    data = [c_web, c_zalo, c_fb]

    c_web_total = MWModel.countTotalByChanel('Web')
    c_zalo_total = MWModel.countTotalByChanel('Zalo')
    c_fb_total = MWModel.countTotalByChanel('FB')
    data_total = [c_web_total, c_zalo_total, c_fb_total]

    rp_week_web = [0, 0, 0, 0, 0, 0, 0]
    rp_week_zalo = [0, 0, 0, 0, 0, 0, 0]
    rp_week_fb = [0, 0, 0, 0, 0, 0, 0]
    in_week = d.weekday()
    for i in range(0, in_week + 1):
        d_w = d + datetime.timedelta(days= -(in_week - i))
        rp_week_web[i] = MWModel.countByChanelFromDayToDay('Web', d_w, d_w)
        rp_week_zalo[i] = MWModel.countByChanelFromDayToDay('Zalo', d_w, d_w)
        rp_week_fb[i] = MWModel.countByChanelFromDayToDay('FB', d_w, d_w)

    bag = {
        'd_chart': json.dumps(data),
        'd_total_chart': json.dumps(data_total),
        'rp_web': json.dumps(rp_week_web),
        'rp_zalo': json.dumps(rp_week_zalo),
        'rp_fb': json.dumps(rp_week_fb)
    }

    return render_template('AdminView/Index.html', page='Dashboard', bag=bag)


@app.route('/admin/history', methods=['POST', 'GET'])
def History():
    if request.method == 'GET':
        history = MWModel.getAll()
        return render_template('AdminView/History.html', page='History', history=history)
    else:
        pass


@app.route('/admin/setting', methods=['POST', 'GET'])
def Setting():
    if request.method == 'GET':
        return render_template('AdminView/Setting.html', page='Setting')
    else:
        fb_vt = request.form.get('fb_vt')
        fb_pat = request.form.get('fb_pat')
        zoi = request.form.get('zoi')
        z_pat = request.form.get('z_pat')
        pass
