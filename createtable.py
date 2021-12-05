def table():
    import mysql.connector
    mydb=mysql.connector.connect(host="localhost",user="root",passwd='ketan',database="Yogya_Fitness_Center")
    mycursor=mydb.cursor()
    mycursor.execute("create table yogya_Fitness_center(rollno int(3) primary key,name varchar(20),age int(2))")
table()
    
