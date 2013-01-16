from sqlalchemy import Column, String, Integer, Boolean, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from dbconnection import engine, session
from datetime import datetime

Base = declarative_base()

class AnswerChoice(Base):
    __tablename__ = 'answerchoice'

    id = Column(Integer, primary_key=true, nullable=False)
    created = Column(DateTime, default=datetime.now, nullable=False) 
    user_id = Column(String,nullable=False)
    answer_id0 = Column(Integer, ForeignKey('answer.id'),nullable=False)
    answer0 = relationship('Answer', foreign_keys=[answer_id0])
    answer_id1 = Column(Integer,ForeignKey('answer.id'),nullable=False)
    answer1 = relationship('Answer', foreign_keys=[answer_id1])
    choice = Column(Boolean,nullable=False)
    
    def by_id(id):
        return session.query(AnswerChoice).filter(Answer.id == id).one()

