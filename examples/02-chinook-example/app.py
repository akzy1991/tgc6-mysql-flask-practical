#import pymysql so that we can connect to mySQL
import pymysql

#import dotenv so that we can open our env files
from dotenv import load_dotenv
load_dotenv()

import os

#actually access the database
conn = pymysql.connect(host='localhost',
                       user=os.environ.get("DB_USER"),
                       password=os.environ.get("DB_PASSWORD"),
                       database="Chinook")

cursor = conn.cursor(pymysql.cursors.DictCursor)

# sql = """
# SELECT * FROM Artist JOIN Album 
# ON Artist.ArtistId = Album.ArtistId
# JOIN Track
# ON Track.AlbumId = Album.AlbumId
# ORDER BY Artist.ArtistId
# LIMIT 10
# """


sql = """
SELECT * FROM Track
"""

cursor.execute(sql)
g = input("Search: ")

print()
for res in cursor:
    if g.lower() in res["Name"].lower():
        print(res["Name"])