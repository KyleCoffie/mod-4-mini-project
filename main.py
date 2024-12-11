from connect_sql import connect_database
import author
import User_operations
import book_operations

def main():
    conn = connect_database()
    if conn is not None:
        
        while True:
            conn = connect_database()

            try:
                cursor = conn.cursor()
                print("\n1. Book Operations. \n2. User Operations. \n3. Author Operations \n4. Quit")
                choice = input("Choose an option: ")
                if choice == '1':
                    book_operations.book_operations(conn,cursor)
                    
                elif choice == '2':
                    User_operations.user_operations(conn,cursor)
                    
                elif choice == '3':
                    author.author_operations(conn,cursor)
                    
                elif choice == '4':
                    break
                else: print("Invalid choice Please try again.")
            except Exception as e:
                    print(f"An error has occured: {e}")
            finally:
                cursor.close()
                conn.close()
        
if __name__ == "__main__":
    main()
            