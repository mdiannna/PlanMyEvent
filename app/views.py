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


def validated(s):
	print s
	try: 
		int(s)

		if int(s)<10000:
			return int(s)
		return -1
	except ValueError:
		return -1	


@app.route("/event", methods=['GET', 'POST'])
def event():
	form = EventForm(request.form, csrf_enabled=True)
	# data=[{'name':'Conference'}, {'name':'Class, Training, or Workshop'}, {'name':'IT event'}]
	error = ""

	data=[]
	dict = {}

	event_types = EventType.query.all()
	keys = ['name', 'name', 'name']
	for i in range(0, len(event_types)):
		dict['name']=event_types[i].name
		data.append(dict.copy())
	
	
	
	if request.method == "POST" :
		budget = validated(str(form.budget.data))
		if(budget < 0):
			error = "Please select a number between 0 and 10000 for your budget"
		elif budget == 0:
			error = "# Are you sure you want to organize an event with 0 money?"
		elif budget>0:
			select = request.form.get('event_type_select')
			print "Select: " + str(select)
			# print "Request sent + form data:" + form.event_type.data
			# return redirect(url_for("/event_options", event_type=form.event_type.data))
			return redirect(url_for("event_options", event_type=select))


		
	return render_template("event.html", form=form, data=data, error=error)


@app.route("/event_options", methods=['GET', 'POST'])
def event_options():
	form = EventForm(request.form, csrf_enabled=True)

	query_name = request.args['event_type']
	event_type_query = EventType.query.filter_by(name=query_name)
	
	event_type = event_type_query[0]

	options = []
	options.append(event_type.venues)
	options.append(event_type.caterers)
	options.append(event_type.stylist_decor)
	options.append(event_type.event_planner)
	options.append(event_type.entertainment)
	options.append(event_type.photographer)
	print "options:"
	print options

	options_name = ['venues', 'caterers', 'stylist_decor', 'event_planner', 'entertainment', 'photographer']
	
	return render_template("event.html", form=form, event_name=event_type_query[0].name, options=options, 
							options_name=options_name)
