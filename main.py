from author import Author
from book_operations import Book
from User_operations import User

library = {}
current_loans = {}
users = {}
catalog = {}


def main():
    

    while True:
        print("\n1. Book Operations. \n2. User Operations. \n3. Author Operations \n4. Quit")
        choice = input("Choose an option: ")
        if choice == '1':
            Book.book_operation(library,current_loans)
            
        elif choice == '2':
            User.user_operations(users)
            
        elif choice == '3':
            Author.author_operations(catalog)
            
        elif choice == '4':
            print("Goodbye thank you for using this program")
            break
        else: print("Invalid choice. Please try again.")
        
        
if __name__ == "__main__":
    main()
            