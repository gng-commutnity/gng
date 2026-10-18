import modules.connection
import modules.basics
con = None
cur = None

def passwd(pas):
    global con, cur
    pw=pas

    con=modules.connection.connection(pw)
    cur=modules.connection.curso(con)

def colname():
    s=modules.basics.alldata(cur,"stock")
    return cur.column_names
def all_data():
    s=modules.basics.alldata(cur,"stock")
    return s
def insert_data(data):
    modules.basics.insertdata(con,cur,"stock",data)
