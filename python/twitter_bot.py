import os
import requests
from auth import get_twitter_conn_v1, get_twitter_conn_v2

path = "IMG_6822.jpg"

# Authenticate to Twitter
client_v1 = get_twitter_conn_v1()
client_v2 = get_twitter_conn_v2()

def upload_image(path):
    media = client_v1.simple_upload(filename=path)        
    media_id = media.media_id

    # Post the tweet with the image and tweet_text
    tweet = client_v2.create_tweet(media_ids=[media_id])

    print("Success - Tweet has been posted")

# Delete the image file after tweeting
#os.remove(media_path)

upload_image(path)



