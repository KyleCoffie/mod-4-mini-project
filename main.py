import book_operations
import author
import User_operations




def main():
    library = {}
    current_loans = []
    while True:
        print("\n1. Book Operations. \n2. User Operations. \n3. Author Operations \n4. Quit")
        choice = input("Choose an option: ")
        if choice == '1':
            book_operations()
            
        elif choice == '2':
            User_operations()
            
        elif choice == '3':
            author()
            
        elif choice == '4':
            break
        else: print("Invalid choice. Please try again.")
        
        
if __name__ == "__main__":
    main()
            