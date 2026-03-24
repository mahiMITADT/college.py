# Program: Library management (basic)

class Library:
    def __init__(self):
        self.books = ["Python", "Java", "C++"]

    def show_books(self):
        print("Available Books:")
        for b in self.books:
            print("-", b)

    def issue_book(self, book):
        if book in self.books:
            self.books.remove(book)
            print("Issued:", book)
        else:
            print("Not available")

    def return_book(self, book):
        self.books.append(book)
        print("Returned:", book)


lib = Library()
lib.show_books()
lib.issue_book("Python")
lib.return_book("Python")
