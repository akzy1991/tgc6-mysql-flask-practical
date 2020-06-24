import pymysql
import os 
from dotenv import load_dotenv

# 1. load the environment variable
load_dotenv()

# 2. create database connection
conn = pymysql.connect(host="localhost",
                       user=os.environ.get("DB_USER"),
                       password=os.environ.get("DB_PASSWORD"),
                       database="Chinook")

# 3. create cursor                       
cursor = conn.cursor(pymysql.cursors.DictCursor)

# 4. define the sql statement

track_name = input("Please enter a track name: ")

sql = f"""
SELECT * FROM Track
WHERE Name LIKE "%{track_name}%" 
LIMIT 10
"""

# 5. Execute the statement

cursor.execute(sql)

# 6. Output the results
for res in cursor:
    print("Track: ", res["Name"])
    print("Composed by : ", res["Composer"])


# # 7. REWIND CURSOR

# cursor.scroll(0,'absolute')