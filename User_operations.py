class User:
    def __init__ (self):
        pass
    
    
    
    while True:
        print("\n1. Book Operations. \n2. User Operations. \n3. Author Operations \n4. Quit")
        choice = input("Choose an option: ")
        if choice == '1':
            book_operations()
            pass
        elif choice == '2':
            user_operations()
            pass
        elif choice == '3':
            author_operations()
            pass
        elif choice == '4':
            break
        else: print("Invalid choice. Please try again.")
    #add a new user
    #view user details
    #display all users