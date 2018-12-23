# -*- coding: utf-8 -*-
from Project import db, app
from sqlalchemy import Column, Integer, String, ForeignKey, BigInteger, Date, ARRAY, Float, DateTime
from sqlalchemy import func, or_, and_, extract, desc
from hashlib import sha1
import datetime


class Config(db.Model):
    __tablename__ = 'config'
    id = Column(Integer, primary_key=True, autoincrement=True)
    key = Column(String)
    value = Column(String)


class Diseases(db.Model):
    __tablename__ = 'diseases'
    id = Column(Integer, primary_key=True)
    tom_tat = Column(String)
    ten = Column(String(250))
    ten_goi_khac = Column(String)
    trieu_chung = Column(String)
    chuan_doan = Column(String)
    dieu_tri_ngan = Column(String)
    tong_quan = Column(String)
    phong_ngua = Column(String)
    dieu_tri = Column(String)
    hinh_anh = Column(ARRAY(String))


class QA(db.Model):
    __tablename__ = 'question_answer'
    id = Column(Integer, primary_key=True, autoincrement=True)
    category = Column(String)
    question = Column(String)
    answer = Column(String)
    cate_fake_id = Column(String)
    cate_slug = Column(String)


class Category(db.Model):
    __tablename__ = 'category'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String)
    slug = Column(String)
    fake_id = Column(String)


class Benh(db.Model):
    __tablename__ = 'songkhoe'
    id = Column(Integer, primary_key=True, autoincrement=True)
    ten = Column(String)
    trieu_chung = Column(String)
    chuan_doan = Column(String)
    nguyen_nhan = Column(String)
    dieu_tri = Column(String)
    phong_tranh = Column(String)
    tong_quan = Column(String)
    fake_id = Column(String)
    do_tuoi = Column(String)  # Gia, tre
    vi_tri = Column(String)
    doi_tuong = Column(String)  # Nam, nu
    chuyen_khoa = Column(String)


class ClientQuery(db.Model):
    __tablename__ = 'client_query'
    id = Column(BigInteger, primary_key=True, autoincrement=True)
    q_date = Column(Date)
    q_time = Column(DateTime)
    request = Column(String)  # Hello
    answer = Column(String)  # Xin chao, ban can ho tro gi
    predicted = Column(String)  # chao_hoi
    accuracy = Column(Float)  # 99%
    chanel = Column(String)  # Zalo, fb, web
    status = Column(String)  # pending / success
    pre_type = Column(String)  # conversation / predict
    solve = Column(String)  # solve problem
    from_u = Column(String)


def getConfig(key):
    return Config.query.filter_by(key=key).first()


def getByID(id):
    return ClientQuery.query.filter_by(id=id).first()


def getAll():
    return ClientQuery.query.all()


def add(cq):
    try:
        db.session.add(cq)
        db.session.commit()
        return cq
    except:
        return None


def update(cq):
    c = getByID(cq.id)
    try:
        c = cq
        db.session.commit()
        return cq
    except:
        return None


def countByChanelInDay(chanel, day):
    rs = ClientQuery.query.filter_by(chanel=chanel)\
        .filter(ClientQuery.q_date == day).count()
    return rs


def countByChanelFromDayToDay(chanel, fr_day, to_day):
    rs = ClientQuery.query.filter_by(chanel=chanel)\
        .filter(ClientQuery.q_date == fr_day).count()
    return rs


def countTotalByChanel(chanel):
    rs = ClientQuery.query.filter_by(chanel=chanel).count()
    return rs


def countByChanelInMonth(chanel, month = datetime.datetime.now().month, year = datetime.datetime.now().year):
    rs = ClientQuery.query.filter_by(chanel=chanel)\
        .filter(and_(extract('year', ClientQuery.q_time) == year, extract('month', ClientQuery.q_time) == month))

    # rs = db.session.query(Table.column, func.count(Table.column)).group_by(Table.column).all()
    rs = rs.query.with_entities(ClientQuery.q_time, func.count(ClientQuery.q_time)).group_by(ClientQuery.q_time).all()
    return rs

