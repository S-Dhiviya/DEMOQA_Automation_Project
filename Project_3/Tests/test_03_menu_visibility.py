# Test Classes contains test scripts and calling actions
# Importing pytest modules to use in test cases
import pytest
# Importing demo page to use methods in it.
from Pages.demo_page import DemoPage


#To use setup fixture from conftest.py
@pytest.mark.usefixtures("setup")
class TestMenuVisibility:

        # test_valid_menu() checks the visibility and clickability of Menu items
        @pytest.mark.positive
        def test_valid_menu(self):
            # This line creates an instance of the DemoPage class, and passes the WebDriver instance (self.driver) to it.
            demo_menu = DemoPage(self.driver)

            # Loops through each menu items stored as dictionary
            for menu_name, locator in demo_menu.MENU_ITEMS.items():
                # element contains the locator value
                element = demo_menu.find_element(locator)

                # Checks each menu is visible and enabled
                assert element.is_displayed(), f"{menu_name} is not visible"
                assert element.is_enabled(), f"{menu_name} is not enabled"
                print(f"{menu_name} is visible and clickable")


        # test_invalid_menu()  fails since dictionary of MENU_ITEMS is accessing only its Key
        @pytest.mark.negative
        def test_invalid_menu(self):
            # This line creates an instance of the DemoPage class, and passes the WebDriver instance (self.driver) to it.
            demo_menu = DemoPage(self.driver)

            # Loops through each menu items stored as dictionary
            for menu_name, locator in demo_menu.MENU_ITEMS.keys():
                # element contains the locator value
                element = demo_menu.find_element(locator)

                # Checks each menu is visible and enabled
                assert element.is_displayed(), f"{menu_name} is not visible"
                assert element.is_enabled(), f"{menu_name} is not enabled"
            print("Error occurs provide proper access to MENU ITEMS")