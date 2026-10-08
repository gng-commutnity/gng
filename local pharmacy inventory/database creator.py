import mysql.connector as my
pwd=input("enter pass: ")
db=my.connect(host="localhost",user="root",passwd=pwd)
cur=db.cursor()
cur.execute("drop database pharmacy") #comment it if for the first time for now
cur.execute("create database pharmacy")
#cur.execute("use pharmacy;")
db.database ="pharmacy"
cur.execute("create table stock(itemcode int, batchno int, mfd date, exp date, stock int);")