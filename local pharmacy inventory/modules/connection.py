import mysql.connector as mysql
def connection(pwd):
    con=mysql.connect(host="localhost",user="root",passwd=pwd)
    return con
def curso(con):
    return con.cursor()