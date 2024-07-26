import os
import requests
from bs4 import BeautifulSoup
from auth import get_twitter_conn_v1, get_twitter_conn_v2
from scraper import scrape_tweets

# Variables
scraped_account = os.getenv('ARCHIVED_USERNAME')                    #holds the username of the account to archive

# Authenticate to Twitter
client_v1 = get_twitter_conn_v1()
client_v2 = get_twitter_conn_v2()

def upload_image(path):
    """Tweets the image from the path"""
    # Gets the Image and formats it through client v1
    media = client_v1.simple_upload(filename=path)        
    media_id = media.media_id

    # Post the tweet with the image through client v2
    try:
        tweet = client_v2.create_tweet(media_ids=[media_id])
        print("Success - Tweet has been posted")
    except Exception as e:
        print("Error - Uploading Media")
        


if __name__ == '__main__':
    # print("Would you like to archive a new account? (yes or no)")
    # print("Would you like to start continuous archival? (yes or no)")
    # print("Enter the account name you want to archive:")

    scrape_tweets(scraped_account)



