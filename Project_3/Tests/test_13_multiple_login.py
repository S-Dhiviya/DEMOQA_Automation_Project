# Importing CSV and OS for file operations
import csv
import os
# Importing pytest modules to use in test cases
import pytest
# Importing books page to use methods in it.
from Pages.books_page import BooksPage


# get_login_data() locates the CSV file and reads the data
def get_login_data():
    login_data=[]
    # Get the directory of the current script
    current_dir=os.path.dirname(__file__)
    # Construct the correct path to the CSV file
    data_file=os.path.join(current_dir,'../Data','invalid_login_data.csv')


    # Read the CSV file
    with open(data_file,newline='') as file:
        reader=csv.DictReader(file)
        for row in reader:
            username=row['username']
            password=row['password']
            login_data.append((username,password))
        return login_data


#To use setup fixture from conftest.py
@pytest.mark.usefixtures("setup")
class TestInvalidLogin:

    # Parameters username and password are used in test function and get_login_data() method is called.
    # This runs multiple times with different sets of invalid username and password
    @pytest.mark.parametrize("username,password",get_login_data())
    def test_invalid_login(self,username,password):
        # This line creates an instance of the BookPage class, and passes the WebDriver instance (self.driver) to it.
        invalid_login = BooksPage(self.driver)
        # Calls login method from BookPage
        invalid_login.login(username,password)
        assert "Valid username or password!" in invalid_login.find_element(invalid_login.LOGIN_OUTPUT).text


