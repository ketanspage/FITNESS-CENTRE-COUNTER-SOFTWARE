# FITNESS-CENTRE-COUNTER-SOFTWARE
def menu():
    print("-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
    for i in range (0,20):
        print("*",end='')
    print("Welcome To The Yogya Fitness Center",end="")
    for i in range (0,20):
        print('*',end='')  
    print("\n-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
    print("""
        menu
        1.show databases
        2.create table
        3.show tables in the database
        4.display structure of the table
        5.add a new column to the table
        6.display records
        7.update an existing record
        8.delete an existing record
        9.exit
        """)
    choice=int(input("Please select your prefered option by typing its Sno."))
    if choice==1:
        import showdatabases
        showdatabases.showdatabases()
    elif choice==2:
        import createtable
        createtable.table()
    elif choice==3:
        import showtables
        showtables.show()
    elif choice==4:
        import desctable
        desctable.desc()
    elif choice==5:
        import insert3
        insert3.adddata()
    elif choice==6:
        import fetchdata
        fetchdata.fetch()
    elif choice==7:
        import update
        update.updatedata()
    elif choice==8:
        import delete
        delete.deletedata()
    elif choice==9:
        print("exiting!!")
        exit()
    else:
        print("wrong input")

menu()
i=6
while i>-1:
    a=input('to enter again please type again')
    if a=='again':
        menu()
        i=i+1
    else:
        print('thanks for visiting')
        break
