# Author : Dexter Drupsteen
# Descrp : Contains controller logic for the hello mvc
# Changes:
# Comment:

from flask import render_template
from models.Question import Question
from dbconnection import session

class Hello():
    def __init__(self):
        # create a few database items
        for model in session.query(Question):
            break
        else:
            session.add(Question("1","What am I?",True))
            session.add(Question("1","Who am I?",True))
            session.add(Question("1","Where am I?",True))
            session.commit()


    def render(self):
        return render_template('index.html',questions=session.query(Question).filter().all())
