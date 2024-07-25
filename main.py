import tweepy
import tkinter as tk
import os
from dotenv import load_dotenv

# Load and store the environment variables
load_dotenv()
consumer_key = os.getenv('CONSUMER_KEY')
consumer_secret = os.getenv('CONSUMER_SECRET')
access_token = os.getenv('ACCESS_TOKEN')
access_token_secret = os.getenv('ACCESS_TOKEN_SECRET')

# Authenticate with Tweepy
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

# tests authentication
try:
    user = api.verify_credentials()
    print("Authentication OK")
except:
    print("Error during authentication")


git config --global user.email "kushpatel2001@gmail.com"
git config --global user.name "Kush Patel"