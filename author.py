from connect_sql import connect_database
  
        
def add_author_dets(cursor,conn):    
    name = input("Enter the author's name: ")
    biography = input("Enter a few words about the author")
    query = "INSERT INTO authors (name,biography) VALUES(%s, %s)"
    cursor.execute(query,(name,biography))
    conn.commit()
    print("New author added successfully. ")
    
def view_author_details(cursor):
    keyword = input("Enter the first name of the author to view details: ")
    query = "SELECT id, name, biography FROM authors WHERE name like %s"
    cursor.execute(query,('%' + keyword + '%',))
    # this is where the query and execute will go
    print("Author details: (Id,Name,bio)")
    for author in cursor.fetchone():
        print(author)
    
        #reserch how to use like in workbench
def display_all(cursor):
    try:
        query = "SELECT * FROM authors"
        print("Here is a list of all of the authors in the system:")
        cursor.execute(query)
        authors = cursor.fetchall()
        if authors:
            for author in authors:
                print(author)
        else:
            print("No authors found in the system. ")   
    except Exception as e:
        print(f"Error has occured {e}")
                
def delete_author(cursor,conn):
    keyword = int(input("Enter the id of the author to delete: "))
    query = "DELETE from authors WHERE id = %s"
    cursor.execute(query, (keyword,))
    conn.commit()
    print(f"Author {keyword} removed successfully.")        

def author_operations(conn,cursor):
    if conn is not None:
        try:
            print("\n1. Add a new author. \n2. View author details. \n3. Display all authors.\n4. Delete an author. ")
            
            choice = input("Choose an option: (1-4): ")
            
            if choice == '1':
                
                add_author_dets(cursor,conn) 
                                
            elif choice == '2':
                view_author_details(cursor)
                    
            elif choice == '3':
                display_all(cursor)
                
            elif choice == '4':
                delete_author(cursor)
                    
            else: print("Invalid choice Please try again.")
        except Exception as e:
                print(f"An error has occured: {e}")
        finally:
            cursor.close()
            conn.close()

               
    