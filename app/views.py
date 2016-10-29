from app import app, db
from app import login_manager
from flask import render_template, request, redirect, url_for
from forms import LoginForm, RegisterForm, EventForm
from app.models import Event, EventType
from flask.ext.login import login_user, login_required, logout_user, current_user
from werkzeug.security import generate_password_hash, check_password_hash



@app.route('/')
def index():
	return render_template("index.html")


def createPackage():
	return 

@app.route("/event", methods=['GET', 'POST'])
def event():
	form = EventForm(request.form, csrf_enabled=True)
	# data=[{'name':'Conference'}, {'name':'Class, Training, or Workshop'}, {'name':'IT event'}]

	data=[]
	dict = {}

	event_types = EventType.query.all()
	keys = ['name', 'name', 'name']
	for i in range(0, len(event_types)):
		dict['name']=event_types[i].name
		data.append(dict.copy())
	# event_type_query = EventType.query.filter_by(name=event_type)
	print "Event types:" 
	print  event_types[0].name
	print "dict name"
	# print dict['name']
	# print "data:" + data
	print "data:"
	print data

	if request.method == "POST":
		select = request.form.get('event_type_select')
		print "Select: " + str(select)
		# print "Request sent + form data:" + form.event_type.data
		# return redirect(url_for("/event_options", event_type=form.event_type.data))
		return redirect(url_for("event_options", event_type=select))


		
	return render_template("event.html", form=form, data=data)


@app.route("/event_options", methods=['GET', 'POST'])
def event_options():
	form = EventForm(request.form, csrf_enabled=True)

	event_type = request.args['event_type']
	event_type_query = EventType.query.filter_by(name=event_type)
	print "ebvent_type_query:"
	print event_type_query[0]
	
	return render_template("event.html", form=form, event_type=event_type_query[0])
