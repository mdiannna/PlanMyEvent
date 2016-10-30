# -*- coding: utf-8 -*-
from flask.ext.wtf import Form
from wtforms import TextField, TextAreaField,  SubmitField, PasswordField, IntegerField, validators
from wtforms.ext.sqlalchemy.fields import QuerySelectField
from models import Event, EventType

# from wtforms import Form
from wtforms_components import DateTimeField, SelectField
from werkzeug.datastructures import MultiDict




class LoginForm(Form):
	key = TextField('Key:')
	username = TextField('Username:')
	password = PasswordField('Password:')
	submit = SubmitField('OK')


class RegisterForm(Form):
	key = TextField('Key:')
	username = TextField('Username:')
	password = PasswordField('Password:')
	firstname = TextField('First name:')
	lastname = TextField('Last name:')
	tel = TextField('Tel. nr:')
	submit = SubmitField('OK')

class EventForm(Form):
	name = TextField('Event name:')
	start_date = TextField('Start date:')
	end_date = TextField('End date:')
	event_type = SelectField('Type', choices=[('pl', 'product launching'), ('be', 'business event'), ('it', 'IT event'), ('cp', 'Christmas party')])
	budget = IntegerField("Budget(in LEI RO ):", [validators.NumberRange(min=0, max=1000)])
	nr_persons = IntegerField('Nr. of persons:')
	description = TextAreaField('Description:')
	scope = TextField("Scope:") 
	submit = SubmitField('OK')


class VendorForm(Form):
	name = TextField('Name:')
	vendor_type = SelectField('Type', choices=[('t1', 'Location')])
	description = TextField('Description:')
	address = TextField('Address:')
	contacts = TextField('Contacts:')


