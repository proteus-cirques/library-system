# library.py

class Book:
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn

    def display_info(self):
        print(f"Title: {self.title}\nAuthor: {self.author}\nISBN: {self.isbn}")
