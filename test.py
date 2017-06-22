import random, string
import tweepy
from textblob import TextBlob
import json, re

# Step 1 - Authenticate
consumer_key= 'sVZQUEr2FKOP9HVgiEex60v4Z'
consumer_secret= 'zha6TPBktaqX6mNHu4Twv04H02VddqcCARwKOUoMgvMIf4fPHr'

access_token='452975600-G90Wq6x2U5qY7cWxFVTWIL1JW2GhqrHBuqiQulON'
access_token_secret='oMIveMb5VrnSqQXGgdQVPP0ejzdyOCVQmRWMiW6daJszy'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

# query string
query = 'INDvSA'
max_tweets = 1
# list of objects containing tweet's data
tweets = [status for status in tweepy.Cursor(api.search, q=query).items(max_tweets)]
print tweets
