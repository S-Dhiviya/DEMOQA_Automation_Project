#BOOKS PAGE for DEMO QA
# Importing By classes from selenium for locators
from selenium.webdriver.common.by import By
# To use the methods from base_page importing Class BasePage.
from Pages.base_page import BasePage
# Importing necessary data from Utils to be used
from Utils.utils import author


#BooksPage inherits BasePage. BooksPage contains locators to be used in test cases.
class BooksPage(BasePage):

    # LOCATORS - Uses find_element() from BasePage to locate these elements while doing interactions.
    # BooksPage locators using XPATH
    BOOKS_API=(By.XPATH,'(//div[@class="category-cards"]//h5)[6]')
    LOGIN=(By.XPATH,'//span[text()="Login"]')

    # Locators to create new user in book store
    NEW_USER=(By.ID,'newUser')
    FIRST_NAME=(By.ID,'firstname')
    LASTNAME=(By.ID,'lastname')
    USERNAME=(By.ID,'userName')
    PASSWORD=(By.ID,'password')
    REGISTER_BUTTON=(By.ID,'register')
    LOGIN_BUTTON=(By.ID,'login')
    LOGIN_OUTPUT=(By.ID,'output')

    # Book store,table and profile locators using XPATH
    BOOK_STORE=(By.XPATH,'//span[text()="Book Store"]')
    TABLE = (By.XPATH, '//div[@class="rt-table"]')
    PROFILE=(By.XPATH,'//span[text()="Profile"]')
    SEARCH_BOX=(By.ID,'searchBox')
    SEARCH_ICON=(By.ID,'basic-addon2')
    SEARCH_TITLE=(By.XPATH,f'//div[@class="rt-td" and text()="{author}"]')


    # METHODS TO INTERACT WITH THE ELEMENTS
    # login() is used to enter credentials and clicks login
    def login(self,username,password):
        self.click_element(self.BOOKS_API)
        self.click_element(self.LOGIN)
        self.enter_text(self.USERNAME,username)
        self.enter_text(self.PASSWORD,password)
        self.click_element(self.LOGIN_BUTTON)


    # new_user_register() is used to create new user to login into book store
    def new_user_register(self,first_name1,last_name1,username,password):
        self.click_element(self.BOOKS_API)
        self.click_element(self.LOGIN)
        self.click_element(self.NEW_USER)
        self.enter_text(self.FIRST_NAME,first_name1)
        self.enter_text(self.LASTNAME,last_name1)
        self.enter_text(self.USERNAME,username)
        self.enter_text(self.PASSWORD,password)
        self.click_element(self.REGISTER_BUTTON)


    # book_store_tables() is used to access the book details in table format
    def book_store_tables(self):
        self.click_element(self.BOOKS_API)
        self.click_element(self.BOOK_STORE)
        self.click_element(self.TABLE)
        table = self.find_element(self.TABLE)
        headers = table.find_elements(By.CLASS_NAME, "rt-resizable-header-content")
        header_text = [header.text.strip() for header in headers]
        print("\nHeaders:", header_text)

        rows = table.find_elements(By.CLASS_NAME, 'rt-tbody')
        for row in rows:
            cols = row.find_elements(By.CLASS_NAME, 'rt-td')
            data = [col.text for col in cols]
            print(data)


    #  book_search() searches the books using book/title/publisher name in Search box
    def book_search(self,author):
        self.click_element(self.BOOKS_API)
        self.click_element(self.BOOK_STORE)
        self.click_element(self.TABLE)
        self.find_element(self.SEARCH_BOX).send_keys(author)
        self.click_element(self.SEARCH_ICON)




