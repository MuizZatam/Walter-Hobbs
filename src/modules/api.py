from dotenv import load_dotenv
from datetime import datetime
import time
import os
import tweepy


load_dotenv()


client = tweepy.Client(

        consumer_key=os.environ.get('API_KEY'),
        consumer_secret=os.environ.get('API_SECRET'),
        access_token=os.environ.get('ACCESS_TOKEN'),
        access_token_secret=os.environ.get('ACCESS_TOKEN_SECRET')
)


def post_tweet(content):

    client.create_tweet(text=content)
