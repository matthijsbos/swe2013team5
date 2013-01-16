from sqlalchemy import Column, String, Integer, Boolean, DateTime
from ../dbconnection import engine, session
from datetime import datetime

Base = declarative_base()

class Answer(Base):
    __tablename__ = 'answer'

    id = Column(Integer, primary_key=True)
    question_id = Column(Integer,ForeignKey('question.id'))
    created = Column(DateTime, default=datetime.now)
    user_id = Column(String, nullable=False)
    answer = Column(String, nullable=False)

    def by_id(id):
        return session.query(Answer).filter(Answer.id == id).one()

