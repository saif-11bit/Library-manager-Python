class Library:
    def __init__(self, book_list, library_name):
        self.book_list = book_list
        self.library_name = library_name
        self.record_lend = {}
    
    def display_book(self):
        print(f"Books in library: {self.book_list}")
    
    def lend_book(self):
        book = input("Enter book name: ").title()
        if book in book_list:
            name = input("Enter your name: ").title()
            self.record_lend[book] = name
            self.book_list.remove(book)
        elif book in self.record_lend:
            print(f"This book is currntly with {str(self.record_lend[book])}")
        elif book not in self.book_list:
            print("This book doesnot exist in library!")

    def add_book(self):
        book = input("Enter book name: ").title()
        self.book_list.append(book)
        print("Succesfully Added!")

    def return_book(self):
        book = input("Enter book name: ").title()
        if book in self.record_lend:
            self.book_list.append(book)
            del self.record_lend[book]
            
        else:
            print("Invalid input!")

if __name__ == "__main__":
    book_list = ["Harry Potter", "Rich Dad PooR Dad", "Think Big", "Friendzoned Love"]
    saif_lib = Library(book_list, "Saif_Library")

    while True:
        user = input("\nD/d for display, L/d to lend, A/a to add book, R/r to return book, Q/q to Quit: ")
        if user == "Q" or user=="q":
            break

        elif user=="D" or user=="d":
            saif_lib.display_book()

        elif user=="L" or user == "l":
            saif_lib.lend_book()

        elif user=="A" or user == "a":
            saif_lib.add_book()

        elif user=="R" or user=="r":
            saif_lib.return_book()
        