from myapp import myapp_obj
from flask import render_template

@myapp_obj.route("/login")
def login():
	return "Login Page!"

@myapp_obj.route("/members/<string:name>/")
def getMember(name):
	return 'Hi ' + name

@myapp_obj.route("/")
def home():
	title = 'Top Cities'
	name = 'Brandon'
	return render_template('home.html', title = title, name = name)
