def show():
    import mysql.connector
    a=mysql.connector.connect(host="localhost",user="root",password="ketan",database='Yogya_Fitness_Center')
    mycursor=a.cursor()
    mycursor.execute("SHOW TABLES")
    for x in mycursor:
        print(x)
