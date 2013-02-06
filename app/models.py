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


class User(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    user = db.Column(db.String(64), unique = True)
    password = db.Column(db.String(500))
    name = db.Column(db.String(500))
    email = db.Column(db.String(120), unique = True)
    # posts = db.relationship('Post', backref = 'author', lazy = 'dynamic')

    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        return unicode(self.id)

    def __repr__(self):
        return '<User %r>' % (self.nickname)
