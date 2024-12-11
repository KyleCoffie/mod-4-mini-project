from connect_sql import connect_database
import random        
import string       

def add_user(cursor,conn):
    name = input("Enter user name: ")
    number = random.randint(10, 99)
    letters = ''.join(random.choice(string.ascii_lowercase) for _ in range(2))
    library_id = (f"{number}{letters}")
    #print(library_id)
    query = "INSERT into users(name,library_id)VALUES (%s,%s)"
    cursor.execute(query,(name,library_id))
    conn.commit()
    print("User successfully created. ")

def display_user_details(cursor):
    keyword = input("Enter the username to view details: ")
    query = "SELECT id, name,library_id FROM users WHERE name like %s"
    cursor.execute(query,(keyword,))
    # this is where the query and execute will go
    print("User details: ")
    for user in cursor.fetchone():
        print(user)
    
def display_users(cursor):
    try:
        query = "SELECT * FROM users"
        print("All users in the system: ")
        cursor.execute(query)
        users = cursor.fetchall()
        if users:
            for user in users:
                print(user)
        else:
            print("No users found in the system. ")
    except Exception as e:
        print(f"Error has occured {e}")
        

def delete_user(cursor,conn):
    keyword = int(input("Enter the id of the user to delete: "))
    query = "DELETE from users WHERE id = %s"
    cursor.execute(query, (keyword,))
    conn.commit()
    print(f"User {keyword} removed successfully.")

def user_operations(conn,cursor):
    if conn is not None:
        try:
            print("\n1. Add a new user. \n2. View user details. \n3. Display all users \n4. Delete user")
            choice = input("Choose an option (1-4): ")
            
            if choice == '1':
                add_user(cursor,conn)
                
                #if user_name:
                   # user = User(user_name)
                   # users[user_name] = user#key is the username value is object user
                   # print(f"{user.username} has been added in the system with Library ID: {user.library_id}")
                    
                #print(users)
            elif choice == '2':
                display_user_details(cursor)                
                
            elif choice == '3':
                display_users(cursor)
                
            elif choice =='4':
                delete_user(cursor,conn)
            
           
        except Exception as e:
            print(f"Error has occured: {e}")
        finally:
            cursor.close()
            conn.close()

    