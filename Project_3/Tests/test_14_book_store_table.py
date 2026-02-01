# Test Classes contains test scripts and calling actions
# Importing pytest modules to use in test cases
import pytest
# Importing books page to use methods in it.
from Pages.books_page import BooksPage
# Importing necessary data from Utils to be used
from Utils.utils import author


#To use setup fixture from conftest.py
@pytest.mark.usefixtures("setup")
class TestBookStore:

    # test_book_store() displays the book details in table format[Book Title,Image,Publisher]
    def test_book_store(self):
        # This line creates an instance of the BookPage class, and passes the WebDriver instance (self.driver) to it.
        book_store=BooksPage(self.driver)
        book_store.book_store_tables()


    # test_book_search() used to search the necessary book/title/publisher using Search box
    def test_book_search(self):
        # This line creates an instance of the BookPage class, and passes the WebDriver instance (self.driver) to it.
        book_store = BooksPage(self.driver)
        book_store.book_search(author)
        book_author=book_store.find_element(book_store.SEARCH_TITLE).text
        assert author==book_author,"Book is not available in store"

