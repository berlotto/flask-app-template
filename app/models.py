# -*- encoding: utf-8 -*-
"""
Python Aplication Template
Licence: GPLv3
"""

from app import db

class ModelExample(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	title = db.Column(db.String(250))
	content = db.Column(db.Text)
	date = db.Column(db.DateTime)

