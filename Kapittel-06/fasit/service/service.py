from repository.register import Register
from model.book_series import BookSeries
from model.book import Book
from model.magazine import Magazine

# Service layer where operations to the register takes place
class Service:

    def __init__(self):
        self.literature = Register().register
    
    def add_literature(self, literature):
        self.literature.append(literature)

    def remove_literature(self, title):
        result = False
        literature = self.find_literature_by_title(title)
        if literature is not None:
            self.literature.remove(literature)
            result = True
        return result
    
    def find_literature_by_title(self, title):
        return next((literature for literature in self.literature if title == literature.title), None)
    
    def find_literature_by_publisher(self, publisher):
            return next((literature for literature in self.literature if publisher == literature.publisher), None)

    def get_number_of_literature(self):
        return len(self.literature)
    
    def return_literature_from_index(self, index):
        if index <= len(self.literature):
            return self.literature[index]
        return None
    
    def find_all_literature_by_publisher(self, publisher):
        return [literature for literature in self.literature if publisher == literature.publisher]

    def find_all_literature_by_author(self, author):
        books = filter(lambda literature: isinstance(literature, Book), self.literature)
        return [book for book in books if author == book.author]

    def find_all_literature_by_type(self, _type):
        magazines = filter(lambda literature: isinstance(literature, Magazine), self.literature)
        return [magazine for magazine in magazines if _type == magazine.type]
    
    def add_book_to_series(self, book_serie, book):
        book_serie.add_book_to_series(book)
    
    def find_books_in_book_serie(self, title):
        book_serie = self.find_literature_by_title(title)
        if isinstance(book_serie, BookSeries):
            return book_serie
        return None
