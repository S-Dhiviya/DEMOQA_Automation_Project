# Elements Page for DEMO QA
# Importing By classes from selenium for locators
from selenium.webdriver.common.by import By
# To use the methods from base_page importing Class BasePage.
from Pages.base_page import BasePage
# Importing ActionChains for mouse and keyboard events
from selenium.webdriver.common.action_chains import ActionChains


#ElementPage inherits BasePage.ElementPage  contains locators to be used in test cases.
class ElementPage(BasePage):

    # LOCATORS - Uses find_element() from BasePage to locate these elements while doing interactions.
    # Element locator using XPATH
    ELEMENTS=(By.XPATH,'//div[@class="category-cards"]//child::h5[1]')

    # Text box locators using XPATH and ID
    TEXT_BOX=(By.XPATH,'//span[text()="Text Box"]')
    FULL_NAME=(By.XPATH,'//input[@id="userName"]')
    EMAIL=(By.ID,'userEmail')
    CURRENT_ADDRESS=(By.ID,'currentAddress')
    PERMANENT_ADDRESS=(By.ID,'permanentAddress')
    SUBMIT=(By.ID,'submit')
    OUTPUT=(By.XPATH,'//div[@id="output"]')

    # Check box locators using XPATH
    CHECK_BOX=(By.XPATH,'//span[text()="Check Box"]')
    HOME_CHECK=(By.XPATH,'//span[@class="rct-checkbox"]')
    INVALID_HOME_CHECK=(By.XPATH,'//span[@class="rct"]')
    CHECKBOX_TEXT=(By.XPATH,'//div[@id="result"]')

    # Radio button locator using XPATH
    RADIO_BUTTON=(By.XPATH,'//span[text()="Radio Button"]')
    RADIO_TEXT=(By.CLASS_NAME,'mt-3')

    # Web Tables locators using XPATH
    WEB_TABLES=(By.XPATH,'//span[text()="Web Tables"]')
    TABLE=(By.XPATH,'//div[@class="rt-table"]')
    FIRST_NAME=(By.XPATH,'//div[text()="First Name"]')

    # Button locators using XPATH and ID
    BUTTONS=(By.XPATH,'//span[text()="Buttons"]')
    DOUBLE_CLICK=(By.ID,'doubleClickBtn')
    DOUBLE_CLICK_TEXT=(By.ID,'doubleClickMessage')
    RIGHT_CLICK=(By.ID,'rightClickBtn')
    CLICK_BUTTON=(By.XPATH,'//button[text()="Click Me"]')
    INVALID_CLICK_BUTTON = (By.XPATH, '//button[text()="Button"]')

    # File upload and download locators
    UPLOAD=(By.XPATH,'//span[text()="Upload and Download"]')
    FILE_UPLOAD=(By.ID,'uploadFile')
    FILE_UPLOAD_PATH=(By.ID,'uploadedFilePath')
    DOWNLOAD=(By.ID,'downloadButton')


    # METHODS TO INTERACT WITH THE ELEMENTS
    # Text box() is used to fill the details and click submit
    def text_box(self,full_name,email,current_address,permanent_address):
        self.click_element(self.ELEMENTS)
        self.click_element(self.TEXT_BOX)
        self.enter_text(self.FULL_NAME,full_name)
        self.enter_text(self.EMAIL,email)
        self.enter_text(self.CURRENT_ADDRESS,current_address)
        self.enter_text(self.PERMANENT_ADDRESS,permanent_address)
        self.click_element(self.SUBMIT)


    # Check_box() is used to check/click the home checkbox
    def check_box(self):
        self.click_element(self.ELEMENTS)
        self.click_element(self.CHECK_BOX)
        self.find_element(self.HOME_CHECK).click()
        print(self.find_element(self.CHECKBOX_TEXT).text)


    # invalid_check_box() is used to test whether home checkbox is clicked or not
    def invalid_check_box(self):
        self.click_element(self.ELEMENTS)
        self.click_element(self.CHECK_BOX)
        self.find_element(self.INVALID_HOME_CHECK).is_selected()


    # fill_radio_options() is used to fill the radio button option from utils.py
    def fill_radio_options(self, radio_button_option):
        return (By.XPATH,f'//label[@class="custom-control-label" and text()="{radio_button_option}"]')


    # Radio button() is used to select the different radio button options
    def radio_button(self,radio_button_option):
        self.click_element(self.ELEMENTS)
        self.click_element(self.RADIO_BUTTON)
        self.find_element(self.fill_radio_options(radio_button_option)).click()
        print(self.find_element(self.RADIO_TEXT).text)


    # fill_invalid_radio_options() is used to fill the radio button option from utils.py
    def fill_invalid_radio_options(self, radio_button_option):
        return (By.XPATH, f'//label[@class="custom" and text()="{radio_button_option}"]')


    # invalid_radio_button() is used to select the invalid radio button options
    def invalid_radio_button(self, radio_button_option):
        self.click_element(self.ELEMENTS)
        self.click_element(self.RADIO_BUTTON)
        self.find_element(self.fill_invalid_radio_options(radio_button_option)).click()
        print(self.find_element(self.RADIO_TEXT).text)


    # Web tables() is used to print the table data
    def web_tables(self):
        self.click_element(self.ELEMENTS)
        self.click_element(self.WEB_TABLES)
        table=self.find_element(self.TABLE)
        headers = table.find_elements(By.CLASS_NAME, "rt-resizable-header-content")
        header_text = [header.text.strip() for header in headers]
        print("\nHeaders:", header_text)

        rows=table.find_elements(By.CLASS_NAME,'rt-tbody')
        for row in rows:
            cols = row.find_elements(By.CLASS_NAME, 'rt-td')
            data = [col.text for col in cols]
            print(data)
        # to print first name
        # rows = self.driver.find_elements(By.CLASS_NAME, "rt-tr-group")
        # for row in rows:
        #     cells = row.find_elements(By.CSS_SELECTOR, ".rt-td")
        #     if cells and cells[0].text.strip():  # First column = First Name
        #         print(cells[0].text)


    # Buttons() is used to click the different buttons using ActionChains
    def buttons(self):
        self.click_element(self.ELEMENTS)
        self.click_element(self.BUTTONS)
        actions=ActionChains(self.driver)
        actions.double_click(self.find_element(self.DOUBLE_CLICK)).perform()
        actions.context_click(self.find_element(self.RIGHT_CLICK)).perform()
        actions.move_to_element(self.find_element(self.CLICK_BUTTON)).click().perform()


    #  invalid_click_on_buttons() is used to invalid clicks on the buttons using ActionChains
    def invalid_click_on_buttons(self):
        self.click_element(self.ELEMENTS)
        self.click_element(self.BUTTONS)
        actions = ActionChains(self.driver)
        actions.move_to_element(self.find_element(self.DOUBLE_CLICK)).click().perform()
        actions.double_click(self.find_element(self.RIGHT_CLICK)).perform()
        actions.move_to_element(self.find_element(self.CLICK_BUTTON)).click().perform()


    # upload_file() is used to upload file from the local machine
    # MAC: /Users/dhiviya/Desktop/my_Project/myfile.txt
    # Windows: C:\Users\dhiviya\Desktop\my_Project\myfile.txt
    def upload_file(self):
        self.click_element(self.ELEMENTS)
        self.click_element(self.UPLOAD)
        self.find_element(self.FILE_UPLOAD).send_keys("/Users/dhiviya/Desktop/my_Project/myfile.txt")
