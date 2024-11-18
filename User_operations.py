import random
import string



class User:
    def __init__ (self,user):
        self.user = user
        self.library_id = library_id
def generate_user_id():
    # Generate a random 2-digit number (between 10 and 99 inclusive)
    number = random.randint(10, 99)
    
    # Generate two random letters (uppercase)
    letters = ''.join(random.choice(string.ascii_lowercase) for _ in range(2))
    
    # Combine the number and letters into the final ID
    library_id = f"{number}{letters}"
    
    return library_id   
library_id = generate_user_id()#TODO 
def user_operations(users):
    
    while True:
        print("\n1. Add a user. \n2. View user details. \n3. Display all users \n4. Quit")
        choice = input("Choose an option: ")
        try:
            generate_user_id()
            if choice == '1':
                
                user = input("Enter user name:")
                print(f"{user} has been added in the system with Library ID: {library_id}")
                
            elif choice == '2':
                display_user_details(users,library_id)
                selection = input("Enter the username to view details")
                if selection == user:
                    print(user)
                
            elif choice == '3':
                display_users(users)
                
            elif choice == '4':
                break
            else: print("Invalid choice. Please try again.")
        except Exception as e:
            print(f"Error has occured: {e}")
    
    
def display_user_details(users, library_id):
    for user in users.values():
        print(f"{user}{library_id}")
        
def display_users(users):
    print(f"{users}")
   