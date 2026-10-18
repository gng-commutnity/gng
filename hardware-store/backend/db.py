import mysql.connector as cox
import csv
import os
from datetime import datetime
import config

def connect():
    return cox.connect(
        host=config.db_host,
        user = config.db_user,
        database = config.db_name,
        passwd = config.db_pass
    )
#for fetch data
def rows(sql):
    conn = connect()
    try:
        cur = conn.cursor()
        cur.execute(sql)
        return cur.fetchall()
    finally:
        conn.close()

def run(sql):
    pass
