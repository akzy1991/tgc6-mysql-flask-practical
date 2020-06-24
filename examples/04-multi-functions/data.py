"""
Step 1 to step 3 of connecting a Python program to a MySQL database
"""

import pymysql
import os
from dotenv import load_dotenv

# 1. load the environment variable
load_dotenv()

# 2. create database connection


def get_conn(host, user, password, database):
    conn = pymysql.connect(host=host,
                           user=user,
                           password=password,
                           database=database)
    return conn

# 3. create cursor


def get_cursor(conn):
    return conn.cursor(pymysql.cursors.DictCursor)
