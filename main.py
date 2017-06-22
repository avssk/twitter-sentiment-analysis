from twitter import store_tweets
from model import Base, Tweet
from flask import Flask, jsonify, request, url_for, abort, g, render_template, request
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy import create_engine


engine = create_engine('sqlite:///tweets.db')

Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()
app = Flask(__name__)
store_tweets()


@app.route("/")
def start():
    tweets = session.query(Tweet).all()
    tweets = [tweet.serialize for tweet in tweets]
    return render_template('index.html', tweets=tweets)

# endpoints for retrieving tweets data from data
@app.route("/postdata", methods = ['POST'])
def send_data():
    tweets = session.query(Tweet).all()
    return jsonify(tweets = [tweet.serialize for tweet in tweets])


if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=5000)
