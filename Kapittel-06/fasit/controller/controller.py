from model.book import Book
from model.magazine import Magazine
from model.book_series import BookSeries
from service.service import Service

# Communication layer between the user interface and logic
class Controller:

    def __init__(self):
        self.service = Service()

    def add_book(self, book):
        return self.service.add_literature(book)

    def add_magazine(self, magazine):
        return self.service.add_literature(magazine)

    def add_book_series(self, book_serie):
        return self.service.add_book_to_series(book_serie)

    def remove_literature(self, title):
        return self.service.remove_literature(title)

    def search_for_literature_title(self, title):
        return self.service.find_literature_by_title(title)
        
    def search_for_literature_author(self, author):
        return self.service.find_all_literature_by_author(author)
        
    def search_for_literature_type(self, _type):
        return self.service.find_all_literature_by_type(_type)

    def search_for_literature_publisher(self, publisher):
        return self.service.find_literature_by_publisher(publisher)

    def search_for_all_literature_publisher(self, publisher):
        return self.service.find_all_literature_by_publisher(publisher)

    def list_all_literatures(self):
        return self.service.literature

    def number_of_literatues(self):
        return self.service.get_number_of_literature()

    def add_book_to_series(self, book_serie, book):
        self.service.add_book_to_series(book_serie, book)

    def list_book_serie(self, title):
        return self.service.find_books_in_book_serie(title)