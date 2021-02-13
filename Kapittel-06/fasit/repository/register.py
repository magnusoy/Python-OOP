from datetime import date

from model.book import Book
from model.magazine import Magazine
from model.book_series import BookSeries

# Acts as a database storing literature
class Register:

    def __init__(self):
        self.register = fill_register()


# Fill the register up with fake data
def fill_register():
    return [
        Book("Title 1", "Author 1", "Publisher 1", "Genre 1", date.today()),
        Book("Title 2", "Author 2", "Publisher 2", "Genre 2", date.today()),
        Book("Title 3", "Author 3", "Publisher 6", "Genre 3", date.today()),
        Book("Title 4", "Author 4", "Publisher 4", "Genre 4", date.today()),
        Book("Title 5", "Author 4", "Publisher 5", "Genre 5", date.today()),
        Book("Title 6", "Author 6", "Publisher 6", "Genre 6", date.today()),
        Magazine("Title 7", "Publisher 7", "Genre 7", "Type 7", 12, date.today()),
        Magazine("Title 8", "Publisher 8", "Genre 8", "Type 7", 11, date.today()),
        Magazine("Title 9", "Publisher 9", "Genre 9", "Type 7", 10, date.today()),
        Magazine("Title 10", "Publisher 10", "Genre 10", "Type 10", 12, date.today()),
        BookSeries("Title 11", "Publisher 11", "Genre 11",  date.today())
    ]
