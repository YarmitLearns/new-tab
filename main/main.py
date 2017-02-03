'''
TODO:
-get notes working
-get prides working
-get links displayed
-switch to mysql
-upload app to python anywhere
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
from datetime import date

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///heatmap.db'
app.config['SECRET_KEY'] = 'yabadaba dubwub'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
TEMPLATES_AUTO_RELOAD = True

