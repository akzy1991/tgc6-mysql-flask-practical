<<<<<<< HEAD
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
=======
# import pymysql so that we can connect to MySQL
import pymysql
import os
# import dotenv so that we open our env files
from dotenv import load_dotenv
load_dotenv()


# actually access the database
conn = pymysql.connect(host='localhost',
                       user=os.environ.get('DB_USER'),
                       password=os.environ.get('DB_PASSWORD'),
>>>>>>> ba5acc2aa03455d8ae00eccb6315446e411f0a31
                       database="Chinook")

cursor = conn.cursor(pymysql.cursors.DictCursor)

<<<<<<< HEAD
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
=======
sql = """
select * from Album
join Artist on Album.ArtistId = Artist.ArtistId
limit 10
"""

cursor.execute(sql)

for each_result in cursor:
    print("Album:", each_result["Title"])
    print("Artist:", each_result["Name"])
>>>>>>> ba5acc2aa03455d8ae00eccb6315446e411f0a31
