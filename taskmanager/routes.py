from flask import render_template
from taskmanager import app, db
from taskmanager.models import Task, Category

#create route for the app
@app.route("/")
def home():
    return render_template("base.html")