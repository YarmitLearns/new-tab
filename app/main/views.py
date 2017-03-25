'''
TODO:
-clean up / delete development folder (now that I'm using
    version control, i should develop from more directly)
-create config file with local and deployed settings
-setup db-migration in case i need to change db
-create log in so people can't change my stuff.
-change delete button into a icon.
-find out why button formacation works in my heat map, but not my note template.
# i don't use var csrf, but somehow i get csrf_token() in my templates. 
'''
from flask import render_template, url_for, redirect, request
from sqlalchemy import desc
from sqlalchemy.sql import func
from datetime import date, datetime
from .. import db
from ..models import Notes, Prides
from . import main
from .forms import NoteForm
from ..email import send_email

@main.route('/', methods=['GET'])
def home():
    notes = Notes.query.filter_by(show=True).all()
    prides = Prides.query.order_by(Prides.p_date.desc()).all()
    form = NoteForm()
    return render_template('new_tab.html', form=form, notes=notes, prides=prides)

@main.route('/changeNote', methods=['POST'])
def new_note():
    form = NoteForm()
    if request.form.get('del_note_id'):
        del_note_id = request.form['del_note_id']
        row = Notes.query.filter_by(id=del_note_id).first()
        setattr(row, 'show', False)
        db.session.add(row)
        db.session.commit()
        return redirect(url_for('main.home'))
    if form.validate_on_submit():
        note = request.form['note']
        row = Notes(note)
        db.session.add(row)
        db.session.commit()
    return redirect(url_for('main.home'))

@main.route('/newp', methods=['POST'])
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
    return redirect(url_for('main.home'))

@main.route('/email')
def email():
    send_email('l34p@tutanota.com', "First Blueprint Test",
                'email/test')
    return "Email sent!"