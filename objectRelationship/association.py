class Library:
    def __init__(self, name):
        self.name = name
        self.books = []

    def add_book(self, book):
        self.books.append(book)

class Book:
    def __init__(self, title):
        self.title = title

lib1 = Library('Jkuat library: juja')
book1= Book('Rich dad poor dad')
book2= Book('Atomic habits')
lib1.add_book(book1)
lib1.add_book(book2)
print(lib1.books)