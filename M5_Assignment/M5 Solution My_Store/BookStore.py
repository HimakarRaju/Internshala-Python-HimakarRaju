
import sqlite3
       

def dbcreate():
    curstore.execute('''CREATE TABLE books (
    TITLE TEXT(30) PRIMARY KEY,
    AUTHOR TEXT(20) NOT NULL,
    PRICE FLOAT,
    COPIES INTEGER);''')
    print("Table Created")
    
def tableinsert():
 
    btitle=input("Enter name of the book: ")
    bauthor=input("Enter author: ")
    bprice=float(input("Enter price: "))
    bcopies=int(input("Enter no. of copies: "))
    curstore.execute("INSERT INTO books(TITLE,AUTHOR,PRICE,COPIES) VALUES (?,?,?,?);", (btitle,bauthor,bprice,bcopies))
    MyStore.commit()
    print("\nRow inserted into books table\n")


MyStore=sqlite3.connect('mybookstore.db')
curstore=MyStore.cursor()

choice =0

while choice != 3:
    print("Table creation and Inserting records into the table\n")
    print("Press 1 to create Table if table is not created\nPress 2 to Insert Records\nPress 3 to Exit\n")
    choice=int(input("Enter choice : "))
    if (choice ==1):
        try:
            dbcreate()
        except:
            print()
    if (choice == 2):
        try:
            tableinsert()
        except:
            print("Enter correct values and try again!\n")

          
MyStore.close()




    
    










