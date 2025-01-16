from flask import render_template
from taskmanager import app, db

#create route for the app
@app.route("/")
def home():
    return render_template("base.html")