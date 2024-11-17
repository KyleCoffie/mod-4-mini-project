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

    def return_book(self):#return a book
        self.__is_available = True

def book_operation(library):
    while True:
        print("\n1.Add Book . \n2. Check Out. \n3. Return Book \n4.Search \n5. Quit")
        choice = input("Choose an option: ")
        if choice == '1':
            add_book(library)            
        elif choice == '2':
            check_out()            
        elif choice == '3':
            return_book()            
        elif choice == '4':
            search_book()
        elif choice == '5':
            break       
        else: print("Invalid choice. Please try again.")
    

 
def add_book(library):#add a new book
      title = input("Enter book title: ")
      author = input("Enter book author: ")
      isbn = input("Enter ISBN: ")
      book = Book(title,author,isbn)# book is an object of the Book class
      library[isbn] = book#able to search for book using the title
      
def check_in(library,current_loans):  
    isbn = input("Enter ISBN of the book to return: ")
    if isbn in library and isbn in current_loans:
        library[isbn].return_book()
        del current_loans[isbn]
        print(f"Book {library[isbn].get_title()} returned")
        
def check_out(library,current_loans):#Borrow a book
    isbn = input("Enter the ISBN of the book to borrow: ")
    user = input("Enter user name: ")
    if isbn in library and library[isbn]:
        current_loans[isbn] = user
        print(f"Book {library[isbn].get_title()} checked out to {user}")
        
def search_book(self,title):#search for a book
    for book in self.books:
        if book.title == title:
            return book
        return None
def display_book(library)#display all books
     for book in library.values():
         print(f"Title: {book.get_title()} Author: {book.get_author()} ")