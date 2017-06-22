from sqlalchemy import Column,Integer,String,ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy import create_engine

Base = declarative_base()

class Tweet(Base):
    __tablename__ = 'issue'
    id = Column(Integer, primary_key=True)
    tweet_text = Column(String)
    sentiment = Column(String)


    @property
    def serialize(self):
        return {
        'id' : self.id,
        'tweet_text' : self.tweet_text,
        'sentiment' : self.sentiment
            }

engine = create_engine('sqlite:///tweets.db')
Base.metadata.create_all(engine)
