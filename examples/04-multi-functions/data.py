"""
<<<<<<< HEAD
Step 1 to step 3 of connecting a Python program to a MySQL database
=======
Step 1 to step 3 of connecting a Python program to a MysQL database
>>>>>>> ba5acc2aa03455d8ae00eccb6315446e411f0a31
"""

import pymysql
import os
from dotenv import load_dotenv

<<<<<<< HEAD
# 1. load the environment variable
load_dotenv()

# 2. create database connection


=======
# 1. LOAD IN THE ENVIRONMENT VARIABLES
load_dotenv()


# 2. CREATE THE DATABASE CONNECTION
>>>>>>> ba5acc2aa03455d8ae00eccb6315446e411f0a31
def get_conn(host, user, password, database):
    conn = pymysql.connect(host=host,
                           user=user,
                           password=password,
<<<<<<< HEAD
                           database=database)
    return conn

# 3. create cursor


def get_cursor(conn):
    return conn.cursor(pymysql.cursors.DictCursor)
=======
                           database=database
                           )
    return conn


# 3. CREATE THE CURSOR
def get_cursor(conn):
    cursor = conn.cursor(pymysql.cursors.DictCursor)
    return cursor
>>>>>>> ba5acc2aa03455d8ae00eccb6315446e411f0a31
