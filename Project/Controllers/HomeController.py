# -*- coding: utf-8 -*-

from flask import render_template, jsonify, request

from Project import *
from Project.Models import *
import datetime


@app.route('/')
def Home():
    db.create_all()
    return render_template('HomeView/Index.html', message=None)


@app.route('/resetdb')
def ResetDB():
    db.drop_all()
    return 'success'
