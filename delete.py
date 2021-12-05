def deletedata():
    import mysql.connector
    a=mysql.connector.connect(host='localhost',user='root',password='ketan',database='yogya_fitness_center')
    mycursor=a.cursor()
    r=int(input("enter rollno"))
    sql="delete from yogya_fitness_center where rollno = %s"
    mycursor.execute(sql,(r,))
    print(mycursor.rowcount,'record delted')
    a.commit()
    
    
