# main.py
from library import Book

def add_book_to_library(library, title, author, isbn):
    book = Book(title, author, isbn)
    library.append(book)
    print(f"Added '{title}' to the library.")

def display_library(library):
    print("\nLibrary Contents:")
    for book in library:
        book.display_info()
        print("---------------")

def main():
    library = []

    add_book_to_library(library, "The Catcher in the Rye", "J.D. Salinger", "978-0-316-76948-0")
    add_book_to_library(library, "To Kill a Mockingbird", "Harper Lee", "978-0-06-112008-4")
    add_book_to_library(library, "1984", "George Orwell", "978-0-452-28423-4")

    display_library(library)

if __name__ == "__main__":
    main()
