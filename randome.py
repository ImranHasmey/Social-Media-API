import mysql.connector
try:
    mydb=mysql.connector.connect(host="localhost",database="sample",user="root",password="8309343286")
    cursor=mydb.cursor()
    cursor.execute("select * from bank")
    res=cursor.fetchall()
    print(res)
    print("connected")
except Exception:
    pass
