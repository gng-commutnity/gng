import mysql.connector as mysql
def connection(pwd):
    con=mysql.connect(host="localhost",user="root",passwd=pwd,database="pharmacy")
    return con
def curso(con):
    return con.cursor()