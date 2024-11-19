
class Author:
    def __init__(self,author,birthday,birthplace,one_book):
        self.author = author
        self.birthday = birthday
        self.birthplace = birthplace
        self.one_book = one_book
        
        
    def add_author_dets(catalog):    
        author = input("Enter the name of the author: ").title()
        birthday = input("Enter the author's birthday: ") 
        birthplace = input("Enter the author's birthplace: ")
        one_book = input("Enter a book by the author: ").title()
        info = Author(author,birthday,birthplace,one_book)

        # save author deets to catalog 
        catalog[author] = info
        # or
        print(f"Author: {author} added to catalog with details. ")
        # return info so you can use info if your if choice == '1' 
        return info 

    def view_author_details(catalog,author_name):
        if author_name in catalog:
            author = catalog[author_name]
            print(f"Author: {author.author}, Birthday: {author.birthday}, Birthplace: {author.birthplace}, Book written: {author.one_book}")
                
        else: print(f"Author {author} not found")
    def display_all(catalog):
        if catalog:
            print("All authors in the catalog:")
            for author in catalog.values():
                print(f"Author: {author.author}, Book: {author.one_book} ")
        else: print("No authors in the system.")

    def author_operations(catalog):
        while True:
            print("\n1. Add a new author. \n2. View author details. \n3. Display all authors \n4. Quit")
            choice = input("Choose an option: ")
            try:
                if choice == '1':
                    # add author deets 
                    # save author deets to catalog 
                    # info = add_author_dets(info) 
                    Author.add_author_dets(catalog) 
                                
                
                elif choice == '2':
                    selection = input("Enter the author to view details: ").title()
                    Author.view_author_details(catalog, selection)
                    
                elif choice == '3':
                    Author.display_all(catalog)
                    
                elif choice == '4':
                    print("Thank you for using this Author program...")
                    break
                else: print("Invalid choice Please try again.")
            except Exception as e:
                print(f"An error has occured: {e}")

if __name__ == "__main__":
    catalog ={}
               
    Author.author_operations(catalog)