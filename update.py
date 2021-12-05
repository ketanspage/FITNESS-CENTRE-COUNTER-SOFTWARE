def updatedata():
    import mysql.connector
    a=mysql.connector.connect(host='localhost',user='root',password='ketan',database='yogya_fitness_center')
    mycursor=a.cursor()
    n=int(input("enter rollno"))
    k=int(input("enter age"))
    sql="update yogya_fitness_center set age =%s where rollno = %s"
    val=(k,n)
    mycursor.execute(sql,val)
    print(mycursor.rowcount,'record update')
    a.commit()
