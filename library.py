# library.py
import os
import json
import datetime

# Initialize book list
books = []

# Initialize borrowed books dictionary
borrowed_books = {}

# Function to add a new book to the library
def add_book():
    title = input("Enter the title of the book: ")
    author = input("Enter the author of the book: ")
    quantity = int(input("Enter the quantity of the book: "))
    book = {"title": title, "author": author, "quantity": quantity}
    books.append(book)
    print("Book added successfully!")

# Function to view all books in the library
def view_books():
    if not books:
        print("No books in the library.")
    else:
        print("Books in the library:")
        for book in books:
            print(f"Title: {book['title']}, Author: {book['author']}, Quantity: {book['quantity']}")

# Function to borrow a book from the library
def borrow_book():
    title = input("Enter the title of the book you want to borrow: ")
    for book in books:
        if book['title'].lower() == title.lower():
            if book['quantity'] > 0:
                borrower_name = input("Enter your name: ")
                department = input("Enter your department: ")
                borrowed_books[book['title']] = {
                    "author": book['author'],
                    "quantity": book['quantity'],
                    "borrower_name": borrower_name,
                    "department": department,
                    "borrow_date": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                }
                book['quantity'] -= 1
                print("Book borrowed successfully!")
            else:
                print("Book is out of stock.")
            return
    print("Book not found in the library.")

# Function to check if a book is borrowed with borrower details
def check_borrowed_with_details():
    title = input("Enter the title of the book: ")
    for book_title, book_info in borrowed_books.items():
        if book_title.lower() == title.lower():
            print(f"Book Title: {book_title}")
            print(f"Author: {book_info['author']}")
            print(f"Quantity: {book_info['quantity']}")
            print(f"Borrower Name: {book_info['borrower_name']}")
            print(f"Department: {book_info['department']}")
            print(f"Borrow Date: {book_info['borrow_date']}")
            return
    print("Book not found or not borrowed.")

# Function to display a list of borrowed and available books
def check_books_status():
    if not borrowed_books:
        print("No books are currently borrowed.")
    else:
        print("Borrowed books:")
        for title, book_info in borrowed_books.items():
            print(f"Title: {title}, Author: {book_info['author']}, Quantity: {book_info['quantity']}, Borrower Name: {book_info['borrower_name']}, Department: {book_info['department']}, Borrow Date: {book_info['borrow_date']}")
    print("\nAvailable books:")
    for book in books:
        print(f"Title: {book['title']}, Author: {book['author']}, Quantity: {book['quantity']}")

# Function to start the library management system
def main():
    while True:
        print("\n--- Library Management System ---")
        print("1. Add a book")
        print("2. View all books")
        print("3. Borrow a book")
        print("4. Check books status")
        print("5. Check borrowed book with details")
        print("6. Exit")

        choice = input("Enter your choice (1/2/3/4/5/6): ")

        if choice == '1':
            add_book()
        elif choice == '2':
            view_books()
        elif choice == '3':
            borrow_book()
        elif choice == '4':
            check_books_status()
        elif choice == '5':
            check_borrowed_with_details()
        elif choice == '6':
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
