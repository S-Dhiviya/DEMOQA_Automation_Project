# Demo Page for DEMO QA
# Importing By classes from selenium for locators
from selenium.webdriver.common.by import By
# To use the methods from base_page importing Class BasePage.
from Pages.base_page import BasePage


#DemoPage inherits BasePage. DemoPage contains locators to be used in test cases.
class DemoPage(BasePage):

    # LOCATORS - Uses find_element() from BasePage to locate these elements while doing interactions.
    # MENU_ITEMS contains the menu items under Demo Page, and it is stored as Dictionary{Key:Value} pair

    MENU_ITEMS={
    "ELEMENTS":(By.XPATH,'//div[@class="category-cards"]//child::h5[1]'),
    "FORMS":(By.XPATH, '(//div[@class="category-cards"]//h5)[2]'),
    "ALERTS":(By.XPATH, '(//div[@class="category-cards"]//h5)[3]'),
    "BOOKS_API":(By.XPATH, '(//div[@class="category-cards"]//h5)[6]')
    }


    # METHOD TO INTERACT WITH THE ELEMENTS
    # get_menu_name() retrieves each menu name
    def get_menu_name(self, name):
        return self.MENU_ITEMS.get(name)