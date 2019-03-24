"""Flask server to run my app on"""
from jinja2 import StrictUndefined
import json

from flask import (Flask, render_template, redirect, request, flash,
                   session, url_for, jsonify)

app = Flask(__name__)

# Required to use Flask sessions and the debug toolbar
app.secret_key = "12345"

# Normally, if you use an indefined variable in Jinja2, it fails
# silently. Fix this so that, instead, it raises an error.
app.jinja_env.undefined = StrictUndefined


@app.route("/")
def show_homepage():
    """ Show the homepage """

    settings = get_settings()
    a_setting = settings[0]
    b_setting =settings[1]

    return render_template("index.html", a_setting=a_setting, 
    									 b_setting=b_setting)

def get_settings():
	""" Read JSON file and get next a,b settings that have not been tested """

	with open("a-b_settings") as json_file:  
	    data = json.load(json_file)
	    for p in data['settings']:
	    	if p["tested"] == False:
	    		return (p["a_setting"], p["b_setting"])


@app.route("/submit", methods=['GET', 'POST'])
def update_log():
	""" Update log with the setting for both A and B and which setting the user chose """

	a_setting = request.form.get("a_setting")
	b_setting = request.form.get("b_setting")
	user_choice = request.form.get("user_choice")
	
	update_log_file(a_setting, b_setting, user_choice)

	return redirect("/")


@app.route("/settings", methods=["GET", "POST"])
def update_settings():

	# open JSON file to write to it
	# update "Tested" value to false
	# Loop over Tested values
	# if Tested is False
	# return those values
	# send to front end

	with open("a-b_settings.json", "w") as settings:
		settings.write
	pass 


def update_log_file(a_setting, b_setting, user_choice):
	# get setting for A
	# get setting for B
	# get checkbox result
	# open log file to write it
	with open("log.txt", "a") as log:
		log.write(f"\n{a_setting}, {b_setting}, {user_choice}")

		

	# Do you have to read the log file before writing to it?
	# Write to log file
	return




if __name__ == '__main__':
    # We have to set debug=True here, since it has to be True at the
    # point that we invoke the DebugToolbarExtension
    app.debug = True
    # make sure templates, etc. are not cached in debug mode
    app.jinja_env.auto_reload = app.debug

    # Use the DebugToolbar
    #DebugToolbarExtension(app)

    app.run(port=5000, host='0.0.0.0')