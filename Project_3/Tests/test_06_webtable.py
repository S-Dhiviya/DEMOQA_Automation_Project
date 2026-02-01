# Test Classes contains test scripts and calling actions
# Importing pytest modules to use in test cases
import pytest
# Importing element page to use methods in it.
from Pages.element_page import ElementPage


#To use setup fixture from conftest.py
@pytest.mark.usefixtures("setup")
class TestTable:

    # test_webtable() displays the details in the web table
    def test_webtable(self):
        #This line creates an instance of the ElementPage class, and passes the WebDriver instance (self.driver) to it.
        element=ElementPage(self.driver)
        element.web_tables()