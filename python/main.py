import os
from dotenv import load_dotenv
import requests
from auth import get_twitter_conn_v1, get_twitter_conn_v2
from scraper import scrape_tweets

# Variables
archived_username = os.getenv('ARCHIVED_USERNAME')                    #holds the username of the account to archive
full_scrape = os.getenv('FULL_SCRAPE')                                #holds if the user wants to start a full archive                                            

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

    #if the environment variable is set to scrape
    if full_scrape == "true":
        scrape_tweets(archived_username)
    else:
        print("No full archive requested.")
    
    
    print("Starting continuous archival.")






