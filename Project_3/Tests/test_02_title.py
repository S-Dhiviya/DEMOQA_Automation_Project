# Test Classes contains test scripts and calling actions
# Importing pytest modules to use in test cases
import pytest
# Importing base page to use methods in it.
from Pages.base_page import BasePage


#To use setup fixture from conftest.py
@pytest.mark.usefixtures("setup")
class TestPageTitle:

        # test_valid_title() checks the page title matches or not
        @pytest.mark.positive
        def test_valid_title(self):
            # This line creates an instance of the BasePage class, and passes the WebDriver instance (self.driver) to it.
            base_page = BasePage(self.driver)
            assert base_page.get_title() == "DEMOQA"
            print(f"Page Title:{base_page.get_title()}")


        # test_invalid_title() fails since the current title doesn't match the given title
        @pytest.mark.negative
        def test_invalid_title(self):
            # This line creates an instance of the BasePage class, and passes the WebDriver instance (self.driver) to it.
            base_page = BasePage(self.driver)
            assert base_page.get_title() == "DEMO", "Incorrect Title"