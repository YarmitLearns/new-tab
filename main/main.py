'''
TODO:
-√transfer sqlite to mysql
-√convert passed Date() into a python datetime object
-√upload app to python anywhere
-√create models / test models
-transfer notes template to shared new-tab template
-get notes working
-get prides working
-get links displayed
-refactor notes
-create log in so people can't change my stuff.

-study math
-excercise
'''

from flask import Flask, render_template, url_for, redirect, request
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from flask_wtf.csrf import CSRFProtect
from wtforms.fields import SubmitField, StringField
from wtforms.validators import InputRequired #charlimit
from sqlalchemy import desc
from datetime import date, datetime
from sqlalchemy.sql import func

app = Flask(__name__)
SQLALCHEMY_DATABASE_URI = "mysql+mysqlconnector://{username}:{password}@{hostname}/{databasename}".format(
    username="yarmit",
    password="my7349pass",
    hostname="yarmit.mysql.pythonanywhere-services.com",
    databasename="yarmit$new-tab")
app.config["SQLALCHEMY_DATABASE_URI"] = SQLALCHEMY_DATABASE_URI
app.config["SQLALCHEMY_POOL_RECYCLE"] = 299
app.config['SECRET_KEY'] = 'yabadaba dubwub'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['TEMPLATES_AUTO_RELOAD'] = True

db = SQLAlchemy(app)

class Notes(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    note = db.Column(db.String(200))
    n_date = db.Column(db.DateTime)

    def __init__(self, note, n_date=None):
        self.note = note
        if n_date==None:
        	n_date = datetime.utcnow()
        self.n_date = n_date

    def __repr__(self):
        return "Time: {}\nNote: {}\n".format(self.note, self.n_date)

class Prides(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	p_date = db.Column(db.Date)
	math = db.Column(db.Integer)
	programming = db.Column(db.Integer)
	exercise = db.Column(db.Integer)

	def __init__(self, p_date, math=0, programming=0, exercise=0):
		self.p_date = p_date
		self.math = math
		self.programming = programming
		self.exercise = exercise

	def __repr__(self):
		return "Date: {}\nMath: {}\nProgramming: {}\nExercise: {}".format(
			self.p_date, self.math, self. programming, self.exercise)

if __name__ == "__main__":
    db.create_all()
    app.run(debug=True)
