class Book:
    def __init__(self,title,author,isbn):
        self.__title = title
        self.__author = author
        self.__is_available = True
        self.__isbn = isbn

    def get_title(self):
        return self.__title
    
    def is_available(self):
        return self.__is_available
    
    def borrow_book(self):
        if self.__is_available:
            self.__is_available = False
            return True
        return False
    
    def get_author(self):
        return self.__author
    
    def get_isbn(self):
        return self.__isbn
    
    def return_book(self):#return a book
        self.__is_available = True

        
# Book operations 
    def add_book(library):#add a new book
        title = input("Enter book title: ").title()
        author = input("Enter book author: ").title()
        isbn = input("Enter ISBN: ")
        book = Book(title,author,isbn)# book is an object of the Book class
        library[isbn] = book#able to search for book using the title
        print(f"Book {title} added successfully. ")
        return book
        
    def check_in(library,current_loans):  
        isbn = input("Enter ISBN of the book to return: ")
        if isbn in library and isbn in current_loans:
            library[isbn].return_book()
            del current_loans[isbn]
            print(f"Book {library[isbn].get_title()} returned")
        else: print("Book not in our system.")
            
    def check_out(library,current_loans):#Borrow a book
        isbn = input("Enter the ISBN of the book to borrow: ")
        user = input("Enter user name: ")
        if isbn in library and library[isbn].is_available():
            current_loans[isbn] = user
            library[isbn].borrow_book()
            print(f"Book '{library[isbn].get_title()}' checked out to {user}")
        else: print("Book not in our system.")

    def search_book(library):#search for a book
        title = input("Enter the title to search for: ")
        book_found = False
        for book in library.values():
            if book.get_title().lower() == title.lower():
                availability = "Available" if book.is_available() else "Not Available"
                print(f"Title: {book.get_title()} Author: {book.get_author()} ISBN: {book.get_isbn()} Status: {availability}  ")#TODO: add is available or not also provide isbn
                book_found = True
        if not book_found: print("Book not found")    
                
    def display_book(library):#display all books
        if library:
            for book in library.values():
                availability = "Available" if book.is_available() else "Not Available"
                print(f"Title: {book.get_title()} Author: {book.get_author()} ISBN: {book.get_isbn()} Status: {availability}")

    def book_operation(library,current_loans):
        while True:
            print("\n1. Add Book\n2. Check Out\n3. Return Book\n4. Search\n5. Display\n6. Quit")
            choice = input("Choose an option: ")
            try:
                if choice == '1':
                    Book.add_book(library)            
                elif choice == '2':
                    Book.check_out(library, current_loans)            
                elif choice == '3':
                    Book.check_in(library,current_loans)            
                elif choice == '4':
                    Book.search_book(library)
                elif choice == '5':
                    Book.display_book(library)
                elif choice == '6':
                    print("Thank you for using this Book program...")
                    break       
                else: print("Invalid choice. Please try again.")
            except Exception as e:
                print(f"An error has occured: {e} ")

if __name__ == "__main__":
    library = {}
    current_loans = {}                
    Book.book_operation(library,current_loans)
    