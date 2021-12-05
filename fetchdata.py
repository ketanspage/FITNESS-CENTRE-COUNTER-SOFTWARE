def fetch():
    import mysql.connector
    a=mysql.connector.connect(host="localhost",user="root",passwd="ketan",database="yogya_fitness_center")
    mycursor=a.cursor()
    mycursor.execute("select*from yogya_fitness_center")
    r=mycursor.fetchall()
    for x in r:
        print(x)
