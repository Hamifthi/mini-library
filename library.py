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

    # function for printing users borrowing history
    def print_users_borrowing_history(self):
        for username, book_names in self.users_borrowing_history.items():
            print(username)
            print(book_names)

    # function for checking if the user exist or not registered
    def check_user_in_library(self, username):
        if username in self.users:
            return True
        else:
            raise ValueError("sorry this user doesn't register in library")
        
    # function for checking if the book exist or borrowed
    def check_book_in_library(self, book_name):
        if book_name in self.books:
            return True
        else:
            raise ValueError("sorry this book doesn't exist in library books or it has been borrowed")

    # function for checking that a user doesn't borrow a book twice
    def check_user_has_the_book(self, username, book_name, borrow_mode = False):
        if borrow_mode:
            if book_name not in self.users_dict[username]:
                return True
            raise ValueError("sorry this user has the book")
        else:
            if book_name in self.users_dict[username]:
                return True
            raise ValueError("sorry this user has returned the book")

    # function for borrowing books
    def borrow_books(self, username, book_name):
        if self.check_user_has_the_book(username, book_name, True):
            if self.check_user_in_library(username) and self.check_book_in_library(book_name):
                self.users_dict[username].append(book_name)
                self.users_borrowing_history[username].append(book_name)
                self.books_dict[book_name] = username
                self.books.remove(book_name)

    # function for returning books
    def return_books(self, username, book_name):
        if self.check_user_in_library(username):
            if self.check_user_has_the_book(username, book_name):
                self.users_dict[username].remove(book_name)
                self.books_dict[book_name] = ''
                self.books.append(book_name)