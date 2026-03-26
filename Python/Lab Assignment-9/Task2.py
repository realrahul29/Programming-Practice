class Book:
    def __init__(self, name):
        self.name = name

class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def show_books(self):
        for b in self.books:
            print(b.name)

lib = Library()
lib.add_book(Book("Python"))
lib.add_book(Book("AI"))

lib.show_books()