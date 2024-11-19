catalog ={}


class Author:
    def __init__(self,author,birthday,birthplace,one_book):
        self.author = author
        self.birthday = birthday
        self.birthplace = birthplace
        self.one_book = one_book
        
        
    def add_author_dets(self):    
        author = input("Enter the name of the author: ").title()
        birthday = input("Enter the author's birthday: ") 
        birthplace = input("Enter the author's birthplace: ")
        one_book = input("Enter a book by the author: ").title()
        info = Author(author,birthday,birthplace,one_book)

        # save author deets to catalog 
        catalog[author] = info
        # or
        print(f"Author: {author} added to ctalog with deets. ")
        # return info so you can use info if your if choice == '1' 
        return info 

    def view_author_details(author):
        for info in catalog.values():
            if info.catalog == author:
                print(f"Author: {info.author}, Birthday: {info.birthday}, Birthplace: {info.birthplace}, Book written: {info.one_book}")
                
            else: print(f"Author {author} not found")
    def display_all(info):
        if catalog:
            print("All authors:")
            for author in catalog.values():
                print(f"Author: {author} ")
        else: print("No authors in the system.")

    def author_operations(info):
        while True:
            print("\n1. Add a new author. \n2. View author details. \n3. Display all authors \n4. Quit")
            choice = input("Choose an option: ")
            try:
                if choice == '1':
                    # add author deets 
                    # save author deets to catalog 
                    # info = add_author_dets(info) 
                    add_author_dets(info) 
                                
                
                elif choice == '2':
                    selection = input("Enter the author to view details: ")
                    view_author_details(info,selection)
                    
                elif choice == '3':
                    display_all(info)
                    
                elif choice == '4':
                    print("Thankyou for using this program.")
                    break
                else: print("Invalid choice Please try again.")
            except Exception as e:
                print(f"An error has occured: {e}")