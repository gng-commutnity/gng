import mysql.connector as my
pwd=input("enter pass: ")
db=my.connect(host="localhost",user="root",passwd=pwd)
cur=db.cursor()
cur.execute("create database pharmacy;")
cur.execute("use pharmacy;")
cur.execute("create table stock(itemcode int, batchno int, mfd date, exp date, stock int")