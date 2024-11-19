catalog ={}


class Author:
    def __init__(self,author,birthday,birthplace,one_book):
        self.author = author
        self.birthday = birthday
        self.birthplace = birthplace
        self.one_book = one_book
    
def author_operations(catalog):
    while True:
        print("\n1. Add a new author. \n2. View author details. \n3. Display all authors \n4. Quit")
        choice = input("Choose an option: ")
        try:#View author details
            if choice == '1':
               add_author_dets(catalog)
               
            elif choice == '2':
                selection = input("Enter the author to view details: ")
                view_author_details(catalog,selection)
                
            elif choice == '3':
                display_all(catalog)
                
            elif choice == '4':
                break
            else: print("Invalid choice. Please try again.")
        except Exception as e:
            print(f"An error has occured: {e}")
    
def add_author_dets(catalog):    
    author = input("Enter the name of the author: ").title()
    birthday = input("Enter the author's birthday: ") 
    birthplace = input("Enter the author's birthplace: ")
    one_book = input("Enter a book by the author: ").title()
    info = Author(author,birthday,birthplace,one_book)

def view_author_details(catalog,author):
    for info in catalog.values():
        if info.catalog == author:
            print(f"Author: {info.author}, Birthday: {info.birthday}, Birthplace: {info.birthplace}, Book written: {info.one_book}")
            return
    print(f"Author {author} not found")
def display_all(catalog):
    if catalog:
        print("All authors:")
        for author in catalog.values():
            print(f"Author: {author} ")
    else: print("No authors in the system.")#Display all authors
