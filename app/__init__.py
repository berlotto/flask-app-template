# -*- encoding: utf-8 -*-
"""
Python Aplication Template
Licence: GPLv3
"""

from flask import Flask
from flask.ext.bootstrap import Bootstrap
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.pymongo import PyMongo
from flask.ext.login import LoginManager

app = Flask(__name__)

#Configuration of application, see configuration.py, choose one and uncomment.
#app.config.from_object('configuration.ProductionConfig')
app.config.from_object('app.configuration.DevelopmentConfig')
#app.config.from_object('configuration.TestingConfig')

bs = Bootstrap(app) #flask-bootstrap
db = SQLAlchemy(app) #flask-sqlalchemy

lm = LoginManager()
lm.setup_app(app)
lm.login_view = 'login'

from app import views, models
