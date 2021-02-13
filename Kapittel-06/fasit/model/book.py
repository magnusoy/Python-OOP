from .literature import Literature

# Represents a book
class Book(Literature):

    def __init__(self, title, author, publisher, genre, date):
        super().__init__(title, publisher, genre, date)
        self.author = author
    
    def __str__(self):
        return f"\nTitle: {self.title}\nAuthor: {self.author}\nPublisher: {self.publisher}\nGenre: {self.genre}\nDate:{self.date}\n"
    
    def __repr__(self):
        return f"\nTitle: {self.title}\nAuthor: {self.author}\nPublisher: {self.publisher}\nGenre: {self.genre}\nDate:{self.date}\n"