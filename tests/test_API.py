
import os
from dotenv import load_dotenv

# tests connection with API
client_v1 = get_twitter_conn_v1()


try:
    client_v1.verify_credentials()
    print("Authentication OK")
except:
    print("Error during authentication with Client v1")


