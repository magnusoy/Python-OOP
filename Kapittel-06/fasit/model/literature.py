# Represents literature
class Literature:

    def __init__(self, title, publisher, genre, date):
        self.title = title
        self.publisher = publisher
        self.genre = genre
        self.date = date
    
    def __str__(self):
        return f"\nTitle: {self.title}\nPublisher: {self.publisher}\nGenre: {self.genre}\nDate:{self.date}\n"
    
    def __repr__(self):
        return f"\nTitle: {self.title}\nPublisher: {self.publisher}\nGenre: {self.genre}\nDate:{self.date}\n"