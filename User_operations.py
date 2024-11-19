import random
import string

users = {}

class User:
    def __init__ (self,username):
        self.username = username
        
        self.library_id = self.generate_user_id()
    def generate_user_id(self):
        # Generate a random 2-digit number (between 10 and 99 inclusive)
        number = random.randint(10, 99)
        
        # Generate two random letters (uppercase)
        letters = ''.join(random.choice(string.ascii_lowercase) for _ in range(2))
        
        # Combine the number and letters into the final ID
        library_id = (f"{number}{letters}")
        
        return library_id   
    #TODO look at where im getting variablesfrom and decide if i want to patch them thru that way.
    #reviewonclasses
    def user_operations(users):
        
        while True:
            print("\n1. Add a user. \n2. View user details. \n3. Display all users \n4. Delete user\n5. Quit")
            choice = input("Choose an option: ")
            try:
                if choice == '1':
                    user_name = input("Enter user name:")
                    if user_name:
                        user = User(user_name)
                        users[user_name] = user#key is the username value is object user
                        print(f"{user.username} has been added in the system with Library ID: {user.library_id}")
                    else: print("Error : Username cannot be empty.")    
                    #print(users)
                elif choice == '2':
                    selection = input("Enter the username to view details: ")
                    User.display_user_details(users,selection)                
                    
                elif choice == '3':
                    User.display_users(users)
                    
                elif choice =='4':
                    user_to_delete = input("Enter the username to delete:")
                        
                    for user in users.values():
                        if user_to_delete == user_name:
                            users.pop(user_name)
                            print(f"User {user_to_delete} has been deleted.")
                            break
                        else: print(f"No user found with username {user_to_delete}")
                
                elif choice == '5':
                    break
                else: print("Invalid choice. Please try again.")
            except Exception as e:
                print(f"Error has occured: {e}")
    def display_user_details(users,username):
        for user in users.values():
            if user.username == username:
                print(f"Username: {user.username}, Library ID: {user.library_id}")
                return
        print(f"User {username} not found")
            
    def display_users(users):
        if users:
            print("All users:")
            for user in users.values():
                print(f"Username: {user.username}, Library ID: {user.library_id}")
        else: print("No users in the system.")
users = {}       
User.user_operations(users)