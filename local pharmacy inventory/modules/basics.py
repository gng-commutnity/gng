def alldata(cur,table):
    cur.execute("select * from %s;"%(table,))
    return cur.fetchall()
def insertdata(con,cur,table,data):
    cur.execute("insert into %s values%s"%(table,data))
    con.commit()