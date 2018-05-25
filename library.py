import numpy as np
class Library:
    def __init__(self, filename = None):
        import numpy as np
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