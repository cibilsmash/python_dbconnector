import mysql.connector

mydb = mysql.connector.connect(
    host= "localhost",
    user= "root",
    password= "Mariaselvam@96",
    database= "pythonlogin"


)

def create_table():

    mycursor = mydb.cursor()

    mycursor.execute("CREATE TABLE customers (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), address VARCHAR(255))")

    print("created")



#create_table()


def view_tables():

    mycursor = mydb.cursor()

    mycursor.execute("SHOW TABLES")

    for x in mycursor:

        print(x)


#view_tables()




def select_table():

    name = input("Enter the Table Name to View : ")
    mycursor = mydb.cursor()
    mycursor.execute("SELECT * FROM " + name )
    myresult = mycursor.fetchall()
    for x in myresult:
        print(x)


#select_table()



def Insert_Table():
    
    name = input("Enter name : ")

    address = input("Enter address : ")

    mycursor = mydb.cursor()
    sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"

    val = (name, address)
    mycursor.execute(sql, val)
    mydb.commit()

#Insert_Table()

def Update_Table():

    table_name = input("Enter the Table Name to Update: ")

    address = input("Enter the data to change: ")

    name = input("Where to Change: ")

    mycursor = mydb.cursor()

    sql = "update " + table_name + " set address = %s where name = %s"

    val = (address,name)

    mycursor.execute(sql, val)

    mydb.commit()

#Update_Table()

def Delete_Table():

    table_name = input("Enter the table name")

    name = input("Enter the Name to delete the row")


    mycursor = mydb.cursor()

    mycursor.execute("DELETE FROM " + table_name+ " WHERE name = %s",(name,))

    mydb.commit()

    print("Deleted")

#Delete_Table()


print("Choose the action on Database\n")

print("Enter 1 to Create table,\n")

print("Enter 2 to List of tables,\n")

print("Enter 3 to Insert table,\n")

print("Enter 4 to View table,\n")

print("Enter 5 to Update table,\n")

print("Enter 6 to Delete table,\n")


action = input("Enter the number: ")

if action == "1":
    create_table()
elif action == "2":
    view_tables()
elif action == "3":
    Insert_Table()
elif action == "4":
    select_table()
elif action == "5":
    Update_Table()
elif action == "6":
    Delete_Table()
else:
    print("You are Out of Options")
    



