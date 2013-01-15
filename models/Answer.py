from sqlAlchemy import Column, String, Integer, Boolean, DateTime
from dbconnection import engine, session

Base = declarative_base()

class Answer(Base):
    __tablename__ = 'answer'

    id = Column(Integer, primary_key=true)
    created = Column(DateTime, default=datetime.now)
    user_id = Column(String)
    answer = Column(String)

    def by_id(id):
        return session.query(Answer).filter(Answer.id == id).one()

