def showdatabases():
    import mysql.connector
    a=mysql.connector.connect(host="localhost",password='ketan',user='root')
    mycursor=a.cursor()
    mycursor.execute("SHOW DATABASES")
    for x in mycursor:
        print(x)

def database():
    import mysql.connector
    a=mysql.connector.connect(host="localhost",user="root",password="ketan")
    mycursor=a.cursor()
    mycursor.execute("create database Yogya_Fitness_Center")
