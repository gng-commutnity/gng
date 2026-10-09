import modules.connection
import modules.basics
pw=input("enter your password: ")
con=modules.connection.connection(pw)
cur=modules.connection.curso(con)

s=modules.basics.alldata(cur,"stock")
for i in s:
    print(i)