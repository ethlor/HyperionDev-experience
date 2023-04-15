import sqlite3

# add books 
def add_book():
    id1 = input("enter id of book: ")
    title = input("Enter title of book: ")
    author = input("Enter author of book: ")
    qty = input("Enter quantity of book: ")
    # inserts information into the table in database
    cursor.execute('''INSERT INTO books(id,Title,Author, Qty)
                 VALUES(?,?,?,?)''', (id1,title,author,qty))
    print("Books succefuly added")

    db.commit()

# update information 
def update_info(id):
    while True:
        change = input("enter field to change 'id','title','author' or 'qty'")
        # checks what field needs to be changed
        if change == "id":
            # gets the information
            change_field = int(input("Enter new id information: "))
            # trys and changes the inforamtion for the specific book but will throw an exeption if the id exists
            try :
                cursor.execute('''UPDATE books SET id = ? WHERE id = ? ''', (change_field,id))
                print('Book data updated!')
                db.commit()
            except Exception:
                print("id already exists. Try again with different id.")
            break
        
        # checks what field is changed and then adds to the field what the user wants 
        elif change =="title":
            change_field = input("Enter new title for book: ")
            cursor.execute('''UPDATE books SET Title = ? WHERE id = ? ''', (change_field,id))
            print('Book data updated!')
            db.commit()
            break

        elif change == "author":
            change_field = input("Enter new auhtor for book: ")
            cursor.execute('''UPDATE books SET Author = ? WHERE id = ? ''', (change_field,id))  
            print('Book data updated!') 
            db.commit()
            break

        elif change=="qty":
            change_field = int(input("Enter new Qty amount for book: "))
            cursor.execute('''UPDATE books SET Qty = ? WHERE id = ? ''', (change_field,id))   
            print('Book data updated!')
            db.commit()
            break

        else: 
            # raises and exeption if the wrong information was input
            print("field does not exist. Try again and please enter 'id', 'title',' author' or 'qty'.")
    

# Delete a record
def delete_book(id1):
    cursor.execute('''DELETE FROM books WHERE id = ? ''', (id1,))
    print('Book id {} deleted'.format(id1))
    db.commit()

# display a selected record
def display_book(id):
    cursor.execute('''SELECT id ,Title, Author,Qty FROM books  WHERE id = ?''',(id,))
    for row in cursor:
    # row[0] returns the first column in the query (id), row[1] returns the Tilte and row[2] returns the Author .
        print('\nid:{}\tTitle:{}\tAuthor:{}\tQty:{}'.format(row[0],row[1],row[2],row[3]))
    
    db.commit()

# can be used for better search function
def search(id1):
    display_book(id1)

try :

    db = sqlite3.connect('ebookstore')
    cursor = db.cursor()

    while True:
        menu = input("\nSelect number for one of the following Options below:\n1.Enter book\n2.Update book\n3.Delete book\n4.Search book\n0.Exit\n:")
        
        if menu == '1' :
            add_book()
        
        elif menu == '2':
            while True:

                id= input("enter id of book to change")
                display_book(id)
                ans = input("is this the book? Enter 'yes' or 'no'.").lower()
                if ans == "yes":     
                    update_info(id)
                    break
                                      
        
        elif menu == '3' :
            id= input("enter id of book to delete")
            display_book(id)
            # iterates the question if the book displayed is the book ot delete
            # until the choice is right
            while True:
                ans = input("is this the book? Enter 'yes' or 'no'.").lower()
                if ans == "yes":  
                    delete_book(id)
                    break

        elif menu == '4' :
            id= input("Enter id of book: ")
            display_book(id)
            

        elif menu == '0':
            db.close()
            exit()

        else:
            print("please enter a proper menu choice")  

except Exception:
    print("connection to dabase cant be made plese fix and try again")

finally:
    db.close()

#cursor.execute('''
 #   CREATE TABLE books (id INTEGER PRIMARY KEY, Title TEXT,
 #                               Author TEXT,Qty INTEGER)     
 # ''') 
