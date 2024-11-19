import book_operations
import author
import User_operations




def main():
    library = {}
    current_loans = {}
    users = {}
    catalog = {}
    while True:
        print("\n1. Book Operations. \n2. User Operations. \n3. Author Operations \n4. Quit")
        choice = input("Choose an option: ")
        if choice == '1':
            book_operations.book_operation(library,current_loans)
            
        elif choice == '2':
            User_operations.user_operations(users)
            
        elif choice == '3':
            author.author_operations(info)
            
        elif choice == '4':
            print("Goodbye thank you for using this program")
            break
        else: print("Invalid choice. Please try again.")
        
        
if __name__ == "__main__":
    main()
            