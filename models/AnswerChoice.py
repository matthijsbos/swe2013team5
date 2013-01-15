from sqlAlchemy import Column, String, Integer, Boolean, DateTime
from dbconnection import engine, session

Base = declarative_base()

class AnswerChoice(Base):
    __tablename__ = 'answerchoice'

    id = Column(Integer, primary_key=true)
    created = Column(DateTime, default=datetime.now) user_id = Column(String)
    answer_id0 = Column(Integer)
    answer_id1 = Column(Integer)
    choice = Column(Boolean)
    
    def by_id(id):
        return session.query(AnswerChoice).filter(Answer.id == id).one()
        
