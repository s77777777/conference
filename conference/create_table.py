#!/usr/bin/env python
# -*- coding:utf-8 -*-

# 该文件仅用于第一次创建表时
from conference import create_app
from conference import db

app = create_app()

with app.app_context():
    db.create_all()
    #db.drop_all()

