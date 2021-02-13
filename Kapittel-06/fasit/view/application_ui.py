from datetime import date

from controller.controller import Controller
from model.book_series import BookSeries
from model.book import Book
from model.magazine import Magazine
from utils.options import *


# The visual user interaction layer
class ApplicationUI:
    APPLICATION = "Application v0.1"

    def __init__(self):
        self.controller = Controller()
    
    def show_menu(self, menu):
        print(f"\n**** {self.APPLICATION} ****\n")

        for menu_item in menu:
            print(menu_item)
        
        max_menu_item_number = len(menu) + 1
        print(f"{max_menu_item_number}. Exit\n")
        print(f"Please choose menu item (1-{max_menu_item_number}): ")

        menu_selection = int(input())
        if (menu_selection < 1) or (menu_selection > max_menu_item_number):
            print("Wrong input")

        return menu_selection
    
    def start(self):
        quit = False

        while not quit:
            menu_selection = self.show_menu(menu_items)
            if menu_selection == Option.ADD_LITERATURE.value:
                self.add_literature()

            elif menu_selection == Option.REMOVE_LITERATURE.value:
                print("Remove literature")
                title = input("Enter title: ")
                if self.controller.remove_literature(title):
                    print("Removed literature")  
                else: 
                    print("No literature found. Please try another")

            elif menu_selection == Option.SEARCH_BY_TITLE.value:
                print("Search for Literature from title:")
                title = input("Enter title: ")
                literature = self.controller.search_for_literature_title(title)
                if literature is not None:
                    print(literature)
                else:
                    print("No literature found. Please try another")

            elif menu_selection == Option.SEARCH_BY_AUTHOR.value:
                print("Search for Literature from author:")
                author = input("Enter author: ")
                literature = self.controller.search_for_literature_author(author)
                if len(literature) > 0:
                    [print(book) for book in literature if book is not None]
                else:
                    print("No literature found.")

            elif menu_selection == Option.SEARCH_BY_TYPE.value:
                print("Search for Literature from type:")
                _type = input("Enter type: ")
                literature = self.controller.search_for_literature_type(_type)
                if literature is not None:
                    print(literature)
                else:
                    print("No literature found. Please try another")

            elif menu_selection == Option.SEARCH_BY_PUBLISHER.value:
                print("Search for one Literature from publisher:")
                publisher = input("Enter publisher: ")
                literatures =  self.controller.search_for_literature_publisher(publisher)
                if len(literatures) > 0:
                    [print(literature) for literature in literatures if literature is not None]
                else:
                    print("No literature found. . Please try another")

            elif menu_selection == Option.ALL_BY_PUBLISHER.value:
                print("Search for all Literature from publisher:")
                publisher = input("Enter publisher: ")
                literature = self.controller.search_for_all_literature_publisher(publisher)
                if literature is not None:
                    print(literature)
                else:
                    print("No literature found. Please try another")

            elif menu_selection == Option.SEARCH_ALL.value:
                print("Listing all Literature: ")
                [print(literature) for literature in self.controller.list_all_literatures()]

            elif menu_selection == Option.TOTAL_NUMBER.value:
                print("Number of Literature's: ")
                print(f"Total number of literature: {self.controller.number_of_literatues()}")

            elif menu_selection == Option.ADD_BOOK_TO_SERIES.value:
                print("Search for Book series from title: ")
                serie_title = input("Enter title: ")
                book_serie = self.controller.search_for_literature_title(serie_title)
                if isinstance(book_serie, BookSeries):
                    print("Search for Book from title to add to serie: ")
                    book_title = input("Enter title: ")
                    book = self.controller.search_for_literature_title(book_title)
                    if isinstance(book, Book):
                        self.controller.add_book_to_series(book_serie, book)
                        print("Book added to serie")
                    else:
                        print("No book found. Please try another")
                else:
                    print("No book series found. Please try another")

            elif menu_selection == Option.SEARCH_BOOK_SERIES.value:
                print("Search for Book series from title: ")
                title = input("Enter title: ")
                book_serie = self.controller.list_book_serie(title)
                if book_serie is not None:
                    print(book_serie)
                else:
                    print("No book series found. Please try another")

            else:
                if self.want_to_quit():
                    quit = True

    def want_to_quit(self):
        quit = False
        print("Sure you want to quit? Press Y for Yes or N for No")
        quit_selection = input()
        if quit_selection.upper() == "Y":
            print(f"Thank you for using {self.APPLICATION} Bye!\n")
            quit = True
        else:
            print("Exit was aborted")
        return quit

    def add_literature(self):
        quit = False
        title = input("\nEnter Title: ")
        publisher = input("\nEnter Publisher: ")
        genre = input("\nEnter Genre: ")
        date = date.today()
        while not quit:
            menu_selection = self.show_menu(add_menu)

            if menu_selection == 1:
                print("Adding new Book to Register: ")
                author = input("\nEnter Author: ")
                literature = self.controller.add_book(Book(title, author, publisher, genre, date))
                quit = True

            elif menu_selection == 2:
                print("Adding new Magazine to Register: ")
                _type = input("\nEnter Type: ")
                releases_per_year = input("\nEnter releases per year: ")
                literature = self.controller.add_magazine(Magazine(title, publisher, genre, _type, releases_per_year, date))
                quit = True

            elif menu_selection == 3:
                print("Adding new Book series to Register: ")
                author = input("\nEnter Author: ")
                literature = self.controller.add_book_series(BookSeries(title, publisher, genre, date))
                quit = True

            else:
                quit = True
                break
