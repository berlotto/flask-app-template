# -*- encoding: utf-8 -*-
"""
Python Aplication Template
Licence: GPLv3
"""

from flask.ext.wtf import Form, TextField, TextAreaField, DateTimeField, PasswordField
from flask.ext.wtf import Required

class ExampleForm(Form):
	title = TextField(u'Título', validators = [Required()])
	content = TextAreaField(u'Conteúdo')
	date = DateTimeField(u'Data', format='%d/%m/%Y %H:%M')
	#recaptcha = RecaptchaField(u'Recaptcha')

class LoginForm(Form):
	user = TextField(u'Usuário', validators = [Required()])
	password = PasswordField(u'Senha', validators = [Required()])
