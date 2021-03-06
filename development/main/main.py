﻿#TODO: Frontend: change delet button into a icon. 
from flask import Flask, render_template, url_for, redirect, request
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms.fields import StringField, SubmitField
from wtforms.validators import InputRequired #charlimit
from flask_wtf.csrf import CSRFProtect
from sqlalchemy import desc
from datetime import date, datetime


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///notes.db'
app.config['SECRET_KEY'] = 'yabadaba dubwub'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['TEMPLATES_AUTO_RELOAD'] = True

db = SQLAlchemy(app)
csrf = CSRFProtect(app)

# TODO: Add an automatically inserted date for each entry.
class Notes(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    note = db.Column(db.String(200))
    n_date = db.Column(db.DateTime)
    show = db.Column(db.Boolean)

    def __init__(self, note, n_date=None, show=True):
        self.note = note
        if n_date==None:
            n_date = datetime.utcnow()
        self.n_date = n_date
        self.show = show

    def __repr__(self):
        return "Time: {}\nNote: {}\nShow: {}\n".format(
            self.note, self.n_date, self.show)

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

class NoteForm(FlaskForm):
    note = StringField('note', validators=[InputRequired()])
    submit = SubmitField('Add Note')

# don't think that i need this.
# class DeleteNoteForm(FlaskForm):
#     submit = SubmitField('X')

@app.route('/', methods=['GET'])
def main():
    notes = Notes.query.filter_by(show=True).all()
    prides = Prides.query.order_by(Prides.p_date.desc()).all()
    form = NoteForm()
    return render_template('newtab.html', form=form, notes=notes, prides=prides)

@app.route('/changeNote', methods=['POST'])
def new_note():
    form = NoteForm()
    if request.form.get('del_note_id'):
        del_note_id = request.form['del_note_id']
        row = Notes.query.filter_by(id=del_note_id).first()
        setattr(row, 'show', False)
        db.session.add(row)
        db.session.commit()
        return redirect(url_for('main'))
    if form.validate_on_submit():
        note = request.form['note']
        row = Notes(note)
        db.session.add(row)
        db.session.commit()
    return redirect(url_for('main'))

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