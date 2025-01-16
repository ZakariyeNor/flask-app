import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
if os.path.exsists("env.py"):
    import env

#Instance of app 
app = Flask(__name__)
app.config["SECRET_KEY"] = os.environ.get("SECRET_KEY"),
app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("DB_URL")

db = SQLAlchemy(app)

from taskmanager import routes