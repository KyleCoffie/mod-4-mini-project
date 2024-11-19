authors ={}


class Author:
    def __init__(self):
        pass
def author():
    
    while True:
        print("\n1. Add a new author. \n2. View author details. \n3. Display all authors \n4. Quit")
        choice = input("Choose an option: ")
        try:#View author details
            if choice == '1':
               author = input("Enter the name of the author: ")
                
            elif choice == '2':
                view_author_details()
                
            elif choice == '3':
                display_all(author)
                
            elif choice == '4':
                break
            else: print("Invalid choice. Please try again.")
        except Exception as e:
            print(f"An error has occured: {e}")
    
    
    def display_all(authors):
        if authors:
            print("All authors:")
            for author in authors.values():
                print(f"Author: {}")
        else: print("No authors in the system.")#Display all authors
    