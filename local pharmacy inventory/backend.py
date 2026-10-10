import modules.connection
import modules.basics
pw=input("enter your password: ")
con=modules.connection.connection(pw)
cur=modules.connection.curso(con)
def colname():
    s=modules.basics.alldata(cur,"stock")
    return cur.column_names
def all_data():
    s=modules.basics.alldata(cur,"stock")
    return s