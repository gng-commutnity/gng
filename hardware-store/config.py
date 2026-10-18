import os


#database

db_host = os.environ.get("db_host","localhost")
db_port = os.environ.get("db_port","3306")
db_user = os.environ.get("db_user","root")
db_pass = os.environ.get("db_pass","12345678")
db_name = os.environ.get("db_name","hardware-store")

#bill details

shop_name = os.environ.get("shop_name","HARDWARE SHOP")
shop_address = os.environ.get("sh_name","Kendriya vidyalaya silchar")
shop_ph = os.environ.get("ph","+91 74993 73893")
