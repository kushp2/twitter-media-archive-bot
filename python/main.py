import os
from dotenv import load_dotenv
import requests
from auth import get_twitter_conn_v1, get_twitter_conn_v2
from scraper import scrape_tweets
from database import close_connection, display_table, fetch_random_tweet, delete_tweet_by_id

# Variables
archived_username = os.getenv('ARCHIVED_USERNAME')                    #holds the username of the account to archive
full_scrape = os.getenv('FULL_SCRAPE')                                #holds if the user wants to start a full archive                                            

# Authenticate to Twitter
client_v1 = get_twitter_conn_v1()
client_v2 = get_twitter_conn_v2()

def tweet_image_from_path(path):
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

def tweet_random_image():
    '''Tweets a random image from the db and deletes it from the db'''
    # Gets a random tweet then parses the data
    tweet = fetch_random_tweet()
    if tweet:
        tweet_id, tweet_text, tweet_date, images_links = tweet
        image_url = images_links.split(', ')[0]
        image_url = image_url.replace('name=small', 'name=large')

        # Downloads the image
        image_path = "temp_image.jpg"
        with open(image_path, 'wb') as img_file:
            img_file.write(requests.get(image_url).content)

        # Tweets the image
        tweet_image_from_path(image_path)
        #delete_tweet_by_id(tweet_id)
        os.remove(image_path)

    else:
        print("No tweets found in the database.")


if __name__ == '__main__':

    #if the environment variable is set to scrape
    if full_scrape == "true":
        print(f"Saving tweets from @{archived_username} the database.")
        scrape_tweets(archived_username)
    else:
        print("No full archive requested.")
    
    print("Starting continuous archival...")

    close_connection()





