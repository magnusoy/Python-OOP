from enum import Enum

# Menu choices
class Option(Enum):
    ADD_LITERATURE = 1
    REMOVE_LITERATURE = 2
    SEARCH_BY_TITLE = 3
    SEARCH_BY_AUTHOR = 4
    SEARCH_BY_TYPE = 5
    SEARCH_BY_PUBLISHER = 6
    ALL_BY_PUBLISHER = 7
    SEARCH_ALL = 8
    TOTAL_NUMBER = 9
    ADD_BOOK_TO_SERIES = 10
    SEARCH_BOOK_SERIES = 11  

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
