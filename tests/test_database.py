import pypyodbc as odbc
import pandas as pd
import os
from dotenv import load_dotenv

#tests database connectivity
load_dotenv()
server = os.getenv('DB_SERVER')
database = os.getenv('DB_NAME')
username = os.getenv('DB_USERNAME')
password = os.getenv('DB_PASSWORD')
connection_string = 'Driver={ODBC Driver 18 for SQL Server};Server='+ server +';Database='+ database +';Uid='+ username +';Pwd='+ password +';Encrypt=yes;TrustServerCertificate=no;Connection Timeout=60;'
conn = odbc.connect(connection_string)

create_table_sql = '''
CREATE TABLE tweets (
    id INT PRIMARY KEY IDENTITY(1,1),
    tweet NVARCHAR(MAX),
    date NVARCHAR(50),
    images NVARCHAR(MAX)
);
'''


insert_value_sql = """
INSERT INTO tweets (tweet, date, images)
VALUES ('', '2024-07-26', 'http://example.com/image1.jpg');
"""

cursor = conn.cursor()
cursor.execute(create_table_sql)
cursor.execute(insert_value_sql)
conn.commit()
cursor.execute('SELECT * FROM tweets')

dataset = cursor.fetchall()
columns = [column[0] for column in cursor.description]
df = pd.DataFrame(dataset, columns=columns)
print(df)