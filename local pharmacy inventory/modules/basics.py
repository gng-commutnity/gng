def alldata(cur,table):
    cur.execute("select * from %s"%(table,))
    return cur.fetchall()