from .literature import Literature

# Represents a magazine
class Magazine(Literature):

    def __init__(self, title, publisher, genre, _type, releases_per_year, date):
        super().__init__(title, publisher, genre, date)
        self.type = _type
        self.releases_per_year = releases_per_year
    
    def __str__(self):
        return f"\nTitle: {self.title}\nPublisher: {self.publisher}\nType: {self.type}\nReleases per year: {self.releases_per_year}\nGenre: {self.genre}\nDate:{self.date}\n"
    
    def __repr__(self):
        return f"\nTitle: {self.title}\nPublisher: {self.publisher}\nType: {self.type}\nReleases per year: {self.releases_per_year}\nGenre: {self.genre}\nDate:{self.date}\n"