from sqlalchemy import Column, String, Integer, Boolean, DateTime
from sqlalchemt.orm import relationship
from ../dbconnection import engine, session
from datetime import datetime

Base = declarative_base()

class AnswerModel(Base):
    __tablename__ = 'answer'

    id = Column(Integer, primary_key=True)
    questionID = Column(Integer,ForeignKey('question.id'))
    question = relationship('question') 
    created = Column(DateTime, default=datetime.now)
    userID = Column(String, nullable=False)
    text = Column(String, nullable=False)

    def __repr__(self):
        return self.text + 'Represent'

    def __str__(self):
        return self.text

    @staticmethod
    def save(questionID,userID,answerText):
        session.add(AnswerModel(questionID=questionID,userID=userID,text=answerText))
        session.commit()

Base.metadata.create_all(engine)



