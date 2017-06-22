
from model import Base, Tweet
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy import create_engine
import unicodedata

engine = create_engine('sqlite:///tweets.db')

Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()

# Store tweets with their sentiments in a database
def store_tweets():
        tweet_text = "Hello how are you"
        sentiment = 'positive'
        newTweet = Tweet(tweet_text= tweet_text, sentiment= sentiment)
        session.add(newTweet)
        session.commit()

store_tweets()
