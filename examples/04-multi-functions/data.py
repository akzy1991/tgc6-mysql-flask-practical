"""
import pymysql
from dotenv import load_dotenv

# 1. LOAD IN THE ENVIRONMENT VARIABLES
load_dotenv()


# 2. CREATE THE DATABASE CONNECTION
def get_conn(host, user, password, database):
    conn = pymysql.connect(host=host,
                           user=user,
                           password=password,
                           database=database
                           )
    return conn


# 3. CREATE THE CURSOR
def get_cursor(conn):
    cursor = conn.cursor(pymysql.cursors.DictCursor)
    return cursor
