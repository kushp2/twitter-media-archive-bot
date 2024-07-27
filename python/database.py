import pypyodbc as odbcv
import pandas as pd
import os
from dotenv import load_dotenv

# DB login credentials
server = os.getenv('DB_SERVER')
database = os.getenv('DB_NAME')
username = os.getenv('DB_USERNAME')
password = os.getenv('DB_PASSWORD')
connection_string = 'Driver={ODBC Driver 18 for SQL Server};Server='+ server +';Database='+ database +';Uid='+ username +';Pwd='+ password +';Encrypt=yes;TrustServerCertificate=no;Connection Timeout=120;'
conn = odbc.connect(connection_string)

create_table_sql = '''
CREATE TABLE tweets (
    id INT PRIMARY KEY IDENTITY(1,1),
    tweet NVARCHAR(MAX),
    date NVARCHAR(50),
    images NVARCHAR(MAX)
);
'''

insert_tweet_sql = """
INSERT INTO tweets (tweet, date, images)
VALUES (?, ?, ?);
"""


def create_table():
    '''Creates a table to hold tweets'''
    try:
        with conn.cursor() as cursor:
            cursor.execute(create_table_sql)
            conn.commit()
    except Exception as e:
        print(f"An error occurred: {e}")

def insert_tweet(tweet_text, tweet_date, images_links):
    '''Adds a tweet to the database'''
    try:
        with conn.cursor() as cursor:
            cursor.execute(insert_tweet_sql, (tweet_text, tweet_date, images_links))
            conn.commit()
    except Exception as e:
        print(f"An error occurred: {e}")

def close_connection():
    '''Closes the database connection'''
    if conn:
        conn.close()
