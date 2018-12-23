# -*- coding: utf-8 -*-

from flask import render_template, jsonify, request
from Project import *
import datetime, json

@app.errorhandler(404)
def page_not_found(e):
    if request.is_xhr:
        return jsonify({'code': 404, 'message': 'Page not found'}), 404
    return render_template('ErrorView/404.html'), 404


@app.errorhandler(400)
def bad_request(e):
    if request.is_xhr:
        return jsonify({'code': 400, 'message': 'Bad Request'}), 400
    return render_template('ErrorView/400.html'), 400


@app.errorhandler(403)
def forbidden(e):
    if request.is_xhr:
        return jsonify({'code': 403, 'message': 'Forbidden'}), 403
    return render_template('ErrorView/403.html'), 403


@app.errorhandler(405)
def method_not_allow(e):
    if request.is_xhr:
        return jsonify({'code': 405, 'message': 'Method not allow'}), 405
    return render_template('ErrorView/405.html'), 405


@app.errorhandler(500)
def internal_server_error(e):
    if request.is_xhr:
        return jsonify({'code': 500, 'message': 'Internal server error'}), 500
    return render_template('ErrorView/500.html'), 500