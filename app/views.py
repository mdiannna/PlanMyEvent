from app import app, db
from app import login_manager
from flask import render_template, request, redirect
from forms import LoginForm, RegisterForm, EventForm
from app.models import Event
from flask.ext.login import login_user, login_required, logout_user, current_user
from werkzeug.security import generate_password_hash, check_password_hash



@app.route('/')
def index():
	return render_template("index.html")


@app.route("/event", methods=['GET', 'POST'])
def event():
	form = EventForm(request.form, csrf_enabled=True)
	if request.method == "POST":
		print "Request sent"
		return render_template("event.html", form=form)	
	return render_template("event.html", form=form)