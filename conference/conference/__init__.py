from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

from .models import *

from conference.views.conference import blue_conference
from conference.views.account import blue_account


def create_app():
    app = Flask(__name__)
    app.secret_key = 'sss'
    app.debug = True
    app.config.from_object('settings.DevelopmentConfig')

    db.init_app(app)

    app.register_blueprint(blue_account)
    app.register_blueprint(blue_conference)

    return app
