from flask import Flask, render_template, url_for, redirect, request
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from flask_wtf.csrf import CSRFProtect
from wtforms.fields import SubmitField, StringField
from sqlalchemy import desc
from datetime import date

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///heatmap.db'
app.config['SECRET_KEY'] = 'yabadaba dubwub'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['TEMPLATES_AUTO_RELOAD'] = True

db = SQLAlchemy(app)
#learn how to apply this lazily
# def create_app():
# 	app = Flask(__name__)
#	csrf.init_app(app)
csrf = CSRFProtect(app)

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

@app.route('/')
def main():
	rows = Prides.query.order_by(Prides.p_date.desc()).all()
	return render_template('pride.html', rows=rows)

#add pride


@app.route('/newp', methods=['POST'])
def new_p():
	buttons = ['math', 'programming', 'exercise']
	for pride_button in buttons:
		if request.form.get(pride_button):
			button_value = int(request.form[pride_button])
			selected_date = request.form['selectedDate']
			s_date_obj = date(int(selected_date[0:4]),
							  int(selected_date[5:7]),
							  int(selected_date[8:10]))
			today_row = Prides.query.filter_by(p_date=s_date_obj).first()
			if not today_row:
				today_row = Prides(s_date_obj, 0,0,0)
			setattr(today_row, pride_button, button_value)
			db.session.add(today_row)
			db.session.commit()
	return redirect(url_for('main'))

if __name__ == "__main__":
	db.create_all()
	app.run(debug=True)


## OK, i've decieded to just use sql to start. i could use sqlalchemy later.



## IF I WANT TO USE A TON OF SHITY WTFORMS EVERY TIME I USE BUTTONS ##
# I wonder if i should just create a new feild for each pride issue
# rather than trying to sort through them while using one field.
# class Pride_Form(FlaskForm):
# 	p_date = StringField()
# 	p_math = SubmitField('Math')
# 	p_programming = SubmitField('Programming')
# 	p_exercise = SubmitField('exercise')

# class Math_Pride(FlaskForm):
# 	math = SubmitField("Math")

# class Programming_Pride(FlaskForm):
# 	programming = SubmitField("Prog")

# class Exercise_Pride(FlaskForm)::
# 	exercise = SubmitField("Exer")		


#LONG TERM TODO:
# I i release this to the public, i must grab the time for my pride heat map from the client's clock
# i could do this by having them send a javascript Date() object via their pride button press.
# I didn't do it this way to begin because i would have to convert that Date() object on server side
# and it's easier to skip that step and just appy the date server side.