# Test Classes contains test scripts and calling actions
# Importing pytest modules to use in test cases
import pytest
# Importing books page to use methods in it.
from Pages.books_page import BooksPage
# Importing necessary data from Utils to be used
from Utils.utils import first_name1,last_name1,username,password


#To use setup fixture from conftest.py
@pytest.mark.usefixtures("setup")
class TestBookLogin:

    # test_new_user() registers new user details and asserts the URL
    # This includes a captcha which has to be selected manually
    @pytest.mark.positive
    def test_new_user(self):
        # This line creates an instance of the BookPage class, and passes the WebDriver instance (self.driver) to it.
        user = BooksPage(self.driver)
        user.new_user_register(first_name1,last_name1,username,password)
        assert "https://demoqa.com/register" in user.get_current_url()


    # test_book_login() logins with newly created user and asserts the login data
    @pytest.mark.positive
    def test_book_login(self):
        # This line creates an instance of the  BookPage class, and passes the WebDriver instance (self.driver) to it.
        login = BooksPage(self.driver)
        login.login(username,password)
        assert "Invalid username or password!" in login.find_element(login.LOGIN_OUTPUT).text