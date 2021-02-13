from .literature import Literature

# Represents a bookseries
class BookSeries(Literature):

    def __init__(self, title, publisher, genre, date):
        super().__init__(title, publisher, genre, date)
        self.number = 0
        self.series = dict()
    
    def add_book_to_series(self, book):
        self.series[self.number] = book
        self.number += 1

    def get_series_size(self):
        return len(self.series)

    def get_books_in_series(self):
        return self.series.values()
    
    def __str__(self):
        return f"\nBookserie: {self.title}\nBooks: {[book if len(self.series.values()) > 0 else 'Tom' for book in self.series.values()]}"
    
    def __repr__(self):
        return f"\nBookserie: {self.title}\nBooks: {[book if len(self.series.values()) > 0 else 'Tom' for book in self.series.values()]}"