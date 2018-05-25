import numpy as np
class Library:
    # initializing different lists and dictionaries
    def __init__(self, filename = None):
        self.users = []
        self.books = []
        self.users_dict = {}
        self.books_dict = {}
        try:
            self.load_borrowing_history(filename)
        except FileNotFoundError as e:
            self.users_borrowing_history = {}
        self.get_users()
        self.get_books()

    # function to read users from a text file
    def get_users(self):
        with open ('users.txt', 'r') as users_file:
            for user in users_file:
                self.users.append(user.rstrip())
                self.users_dict[user.rstrip()] = []
                self.users_borrowing_history[user.rstrip()] = []

    # function to read books from a text file
    def get_books(self):
        with open ('books.txt', 'r') as books_file:
            for book in books_file:
                self.books.append(book.rstrip())
                self.books_dict[book.rstrip()] = ''    
    
    # function for printing users
    def print_users(self):
        print([user for user in self.users])
        
    # function for printing books
    def print_books(self):
        print([book for book in self.books])

    # function for adding users
    def add_user(self, username):
        self.users.append(username)
        self.users_dict[username] = []
        self.users_borrowing_history[username] = []
        
    # function for adding books
    def add_book(self, book_name):
        self.books.append(book_name)
        self.books_dict[book_name] = ''