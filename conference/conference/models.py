#!/usr/bin/env python
# -*- coding:utf-8 -*-
from . import db


class UserInfo(db.Model):
    """
    用户表
    """
    __tablename__ = 'userinfo'
    id = db.Column(db.Integer, primary_key=True,autoincrement=True)
    name = db.Column(db.String(32), unique=True, nullable=False)
    password = db.Column(db.String(32), nullable=False)
    phone = db.Column(db.String(11), nullable=False)

    # def __repr__(self):
    #     return '<User %r>' % self.name

class Homes(db.Model):
    """
    会议室表
    """
    __tablename__ = 'homes'
    id = db.Column(db.Integer, primary_key=True,autoincrement=True)
    name = db.Column(db.String(32), unique=True, nullable=False)



class ConferenceTime(db.Model):
    """
    时间段表
    """
    __tablename__ = 'conference_time'
    id = db.Column(db.Integer, primary_key=True,autoincrement=True)
    start_time = db.Column(db.Time())
    end_time = db.Column(db.Time())

class Record(db.Model):
    """
    时间段表
    """
    __tablename__ = 'record'
    id = db.Column(db.Integer, primary_key=True,autoincrement=True)
    conference_date = db.Column(db.Date())      # 会议日期
    homes_id = db.Column(db.Integer,db.ForeignKey('homes.id'),nullable=False)
    user_id = db.Column(db.Integer,db.ForeignKey('userinfo.id'),nullable=False)
    conference_time_id = db.Column(db.Integer,db.ForeignKey('conference_time.id'),nullable=False)

    user = db.relationship('UserInfo',backref='records',)

    __table_args__=(
        db.UniqueConstraint('homes_id',conference_date,'conference_time_id'),
    )

    # homes = db.relationship('Homes',db.backref('records'))






