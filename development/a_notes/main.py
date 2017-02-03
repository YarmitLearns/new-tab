#TODO: Frontend: change delet button into a icon. 
#                add css
#TODO: Backend: add button to delete a note.
#
#TODO: Make use of my DeleteNoteForm class within the notes.html template.
from flask import Flask, render_template, url_for, redirect, request
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms.fields import StringField, SubmitField
from wtforms.validators import InputRequired #charlimit
from sqlalchemy import desc


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///notes.db'
app.config['SECRET_KEY'] = 'yabadaba dubwub'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# TODO: Add an automatically inserted date for each entry.
class Notes(db.Model):
    '''A single Note'''
    id = db.Column(db.Integer, primary_key=True)
    note = db.Column(db.String(200))

    def __init__(self, note):
        self.note = note

    def __repr__(self):
        return self.note

# TODO: Maybe add a priority buton as well.
class NoteForm(FlaskForm):
    note = StringField('note', validators=[InputRequired()])
    submit = SubmitField('Add Note')

class DeleteNoteForm(FlaskForm):
    submit = SubmitField('X')

@app.route('/', methods=['GET'])
def main():
    notes = Notes.query.all()
    # notes = Notes.query.order_by(Notes.id.desc())
    form = NoteForm()
    return render_template('notes.html', form=form, notes=notes)

@app.route('/new', methods=['get', 'POST'])
def new_note():
    form = NoteForm()
    if request.form.get('note_id'): #this is to delete, i should rename this.
        note_id = request.form['note_id']
        row = Notes.query.filter_by(id=note_id).first()
        db.session.delete(row)
        db.session.commit()
        return redirect(url_for('main'))
    if form.validate_on_submit():
        note = request.form['note'] #need to import request
        row = Notes(note)
        db.session.add(row)
        db.session.commit()
    return redirect(url_for('main'))


if __name__ == "__main__":
    db.create_all()
    app.run(debug=True)