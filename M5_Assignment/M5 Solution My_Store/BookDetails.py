import sqlite3

def tablefetch():
    booklist=curstore.execute("select * from books")
    for record in booklist:
         print (record)
 
def tableprocess():
    btitle=input("Enter name of the book: ")
    bcopies=int(input("Enter no. of copies: "))
    curstore.execute("select * from books where title= '"+btitle+"';")
    try:
        record=curstore.fetchone()
        bprice=record[2]
        totalprice=bcopies*bprice
        print("Total price = ",totalprice)
    except:
        print("Enter correct values and try again!")
        tableprocess()
    
     
MyStore=sqlite3.connect('mybookstore.db')
curstore=MyStore.cursor()
choice=0
while choice != 3:
    print("\nFetching records from the books table\n")
    print("Press 1 To fetch the records\nPRESS 2 To calculate total price\nPress 3 to Exit\n")
    choice=int(input("Enter choice :"))
    if choice == 1:
        tablefetch()
    else:
        if choice == 2:
            tableprocess()
MyStore.close()
        

