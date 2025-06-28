from dotenv import load_dotenv
from os import environ
import tweepy


load_dotenv()


client = tweepy.Client(

        consumer_key=environ.get('API_KEY'),
        consumer_secret=environ.get('API_SECRET'),
        access_token=environ.get('ACCESS_TOKEN'),
        access_token_secret=environ.get('ACCESS_TOKEN_SECRET')
)


def post_tweet(content):

    client.create_tweet(text=content)
