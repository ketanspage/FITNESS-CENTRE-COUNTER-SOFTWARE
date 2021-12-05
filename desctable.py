def desc():
    import mysql.connector
    a=mysql.connector.connect(host="localhost",user="root",password="ketan",database="Yogya_Fitness_Center")
    mycursor=a.cursor()
    mycursor.execute("DESC Yogya_Fitness_Center")
    for x in mycursor:
        print(x)
    
