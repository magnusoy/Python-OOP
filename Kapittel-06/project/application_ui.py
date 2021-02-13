from register import Register

menu_items = [
        "1.  Add Literature",
        "2.  Remove Literature",
        "3.  Search for Literature's by Title",
        "4.  Search for Literature's by Author",
        "5.  Search for Literature's by Type",
        "6.  Search for Literature's by Publisher",
        "7.  Search for All Literature's by Publisher",
        "8.  List all Literature's",
        "9.  Number of Literature's",
        "10. Add book to series",
        "11. List book serie"
]

add_menu = [
    "1. Add Book",
    "2. Add Magazine",
    "3. Add Book serie"
]

class ApplicationUI:
    APPLICATION = "Application v0.1"

    def __init__(self):
        self.register = Register()
    
    def show_menu(self, menu):
        print(f"\n**** {self.APPLICATION} ****\n")

        for menu_item in menu:
            print(menu_item)
        
        max_menu_item_number = len(menu) + 1
        print(f"{max_menu_item_number}. Exit\n")
        print(f"Please choose menu item (1-{max_menu_item_number}: ")

        menu_selection = int(input())
        if (menu_selection < 1) or (menu_selection > max_menu_item_number):
            print("Wrong input")

        return menu_selection
    
    def start(self):
        quit = False

        while not quit:
            menu_selection = self.show_menu(menu_items)
            if menu_selection == 1:
                self.add_literature()
                pass
            elif menu_selection == 2:
                self.remove_literature()
                pass
            elif menu_selection == 3:
                self.search_for_literature_title()
                pass
            elif menu_selection == 4:
                self.search_for_literature_author()
                pass
            elif menu_selection == 5:
                self.search_for_literature_type()
                pass
            elif menu_selection == 6:
                self.search_for_literature_publisher()
                pass
            elif menu_selection == 7:
                self.search_for_all_literature_publisher()
                pass
            elif menu_selection == 8:
                self.list_all_literatures()
                pass
            elif menu_selection == 9:
                self.number_of_literatues()
                pass
            elif menu_selection == 10:
                self.add_book_to_series()
                pass
            elif menu_selection == 11:
                self.list_book_serie()
                pass
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
        pass

    def remove_literature(self):
        pass

    def search_for_literature_title(self):
        pass

    def search_for_literature_author(self):
        pass

    def search_for_literature_type(self):
        pass

    def search_for_literature_publisher(self):
        pass

    def search_for_all_literature_publisher(self):
        pass

    def list_all_literatures(self):
        pass

    def number_of_literatues(self):
        pass

    def add_book_to_series(self):
        pass

    def list_book_serie(self):
        pass