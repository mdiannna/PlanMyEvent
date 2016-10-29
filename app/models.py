from werkzeug.security import generate_password_hash, check_password_hash
from flask.ext.login import UserMixin
from app import db




class Event(db.Model):
	__tablename__ = "event"
	id = db.Column(db.Integer, primary_key=True)
	event_type = db.relationship('EventType', backref=db.backref('event_type', lazy='dynamic', order_by = id))
	budget = db.Column(db.Integer)
	nr_persons = db.Column(db.Integer)
	description = db.Column(db.Text())
	scope = db.Column(db.String(255))


class EventType():
	__tablename__='event_type'
	id = db.Column(db.Integer, primary_key=True)
	name=db.Column(db.String(255))
	venues=db.Column(db.Boolean())
	caterers=db.Column(db.Boolean())
	audio_visual=db.Column(db.Boolean())
	stylist_decor=db.Column(db.Boolean())
	event_planner=db.Column(db.Boolean())
	entertainment=db.Column(db.Boolean())
	photographer=db.Column(db.Boolean())
