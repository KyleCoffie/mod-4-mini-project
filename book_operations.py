from connect_sql import connect_database
import random
import string
  
# Book operations 
def add_book(cursor,conn):#add a new book
    
    title = input("Enter the book title: ")
    author = input("Enter the author: ")
    isbn = ''.join(random.choice(string.ascii_lowercase) for _ in range(6)) 
    publication_date = input("Enter the publication date in the format (YYYY-MM-DD): ")
    available = True
    query = "INSERT into books (title,author,isbn,publication_date,availability) VALUES(%s, %s,%s,%s,%s)"
    cursor.execute(query,(title,author,isbn,publication_date,available))
    conn.commit()
    print("New book added successfully. ")
    
def check_out(cursor,conn):#Borrow a book
    try:
        user_id = input("Enter your user_id: ")
        book_id = input("Enter the book_id for the book to borrow: ")
        borrow_date = input("Enter the borrow date: Format (YYYY-MM-DD): ")
        return_date = input("Enter the date to return the book: Format (YYYY-MM-DD):")
        availability = False
        query1 = "INSERT into borrowed_books (user_id,book_id,borrow_date,return_date,availability) VALUES (%s,%s,%s,%s,%s)"
        cursor.execute(query1,(user_id,book_id,borrow_date,return_date,availability))
        conn.commit()
        query2 = "UPDATE books SET availibilty = '0' WHERE book_id = %s"
        cursor.execute(query2,(book_id,))
        conn.commit()
        print(f"User_id: {user_id} successfully checked out book with id number: {book_id}")
    except Exception as e: print(f"Error has occured {e}\n Please make sure your are using a valid user_id,book_id nd correct date format.")
        
def check_in(cursor,conn):  
    try:        
        user_id = input("Enter your user_id: ")
        book_id = input("Enter the book_id for the book to return: ")
        query = "DELETE FROM borrowed_books WHERE user_id = %s AND book_id = %s"
        cursor.execute(query,(user_id,book_id))
        conn.commit()
        query2 = "UPDATE books SET availability = '1' WHERE book_id = %s" 
        cursor.execute(query2,(book_id,))
        print(f"User_id: {user_id} successfully checked in book with id number: {book_id}")  
    except Exception as e: print(f"Error has occured {e}\n Please check that your user_id and the book_id are correct. ")

def search_book(cursor):#search for a book
    try:
        keyword = input("Enter the title: ")
        query = "SELECT id, title, isbn,publication_date, availability FROM books WHERE title like %s"
        print("Book details: ")
        cursor.execute(query,('&' + keyword + '%',))
        books = cursor.fetchone()
        if books:
            for book in books:
                print(book)
        else: print("Book not found")
    except Exception as e:
        print(f"Error {e}")
            
def display_books(cursor):#display all books
    try:
        query = "SELECT * FROM books"
        print("All books in the system: ")
        cursor.execute(query)
        books = cursor.fetchall()
        if books:
            for book in books:
                print(book)
        else:
            print("No books found in the system. ")
    except Exception as e:
        print(f"Error has occured {e}")

    
            
            
def book_operations(conn,cursor):
    if conn is not None:
        try:
            print("\n1. Add a new book\n2. Borrow a book\n3. Return a book\n4. Search for a book\n5. Display all books")
            choice = input("Choose an option: ")
            if choice == '1':
                add_book(cursor,conn)   
            elif choice == '2':
                check_out(cursor,conn)            
            elif choice == '3':
                check_in(cursor,conn)            
            elif choice == '4':
                search_book(cursor)
            elif choice == '5':
                display_books(cursor)
                
            else: print("Invalid choice. Please try again.")
        except Exception as e:
            print(f"An error has occured: {e} ")
        finally:
            conn.close()
            cursor.close()
            
                
                
    