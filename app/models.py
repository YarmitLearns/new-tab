from . import db
from datetime import datetime

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
