def adddata():
    import mysql.connector
    mydb=mysql.connector.connect(host="localhost",user="root",passwd="ketan",database="yogya_fitness_center")
    mycursor=mydb.cursor()
    r=int(input("enter the rollno"))
    n=input("enter name")
    m=int(input("enter age"))
    mycursor.execute("INSERT INTO yogya_fitness_center(rollno,name,age) VALUES({},'{}',{})".format(r,n,m))
    mydb.commit()
    print(mycursor.rowcount,"RECORD INSERTED")
    a=mycursor.execute("desc yogya_fitness_center")

