from flask_wtf import FlaskForm
from wtforms.fields import SubmitField, StringField
from wtforms.validators import InputRequired #charlimit

class NoteForm(FlaskForm):
    note = StringField('note', validators=[InputRequired()])
    submit = SubmitField('Add Note')