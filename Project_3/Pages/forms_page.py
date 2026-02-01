# Forms Page for DEMO QA
# Importing By classes from selenium for locators
from selenium.webdriver.common.by import By
# To use the methods from base_page importing Class BasePage.
from Pages.base_page import BasePage
# Importing ActionChains for mouse and keyboard events
from selenium.webdriver.common.action_chains import ActionChains
# Importing Keys to send commands through keyboards
from selenium.webdriver.common.keys import Keys


#FormsPage inherits BasePage. FormsPage contains locators to be used in test cases.
class FormsPage(BasePage):

    # LOCATORS - Uses find_element() from BasePage to locate these elements while doing interactions.
    # Forms Page locators using XPATH and ID
    FORMS=(By.XPATH,'(//div[@class="category-cards"]//h5)[2]')
    PRACTICE_FORM = (By.XPATH, '//span[text()="Practice Form"]')
    FIRST_NAME=(By.ID,'firstName')
    LAST_NAME=(By.ID,'lastName')
    EMAIL=(By.ID,'userEmail')
    MOBILE=(By.ID,'userNumber')

    DOB=(By.ID,'dateOfBirthInput')
    SUBJECTS=(By.ID,"subjectsInput")
    ADDRESS=(By.ID,'currentAddress')
    STATE=(By.ID,'state')
    CITY=(By.ID,'react-select-4-input')
    SUBMIT=(By.ID,'submit')


    # METHODS TO INTERACT WITH THE ELEMENTS
    # fill_gender_options() is used to fill the gender option from utils.py
    def fill_gender_options(self,gender_option):
        return  (By.XPATH, f'//label[text()="{gender_option}"]')


    # fill_hobbies_options() is used to fill the hobby option from utils.py
    def fill_hobbies_options(self, hobby):
        return (By.XPATH, f'//div//label[text()="{hobby}"]')


    # fill_state() is used to fill the State from utils.py
    def fill_state(self,state):
        return (By.XPATH, f'//div[contains(@id,"react-select-3-option") and text()="{state}"]')


    # fill_city() is used to fill the City from utils.py
    def fill_city(self,city):
        return (By.XPATH, f'//div[@id="react-select-4-input" and text()="{city}"]')


    # student_form() is used to fill the student details
    def student_form(self,first_name,last_name,email,gender,mobile,dob,subject,hobby,address,state,city):
        self.click_element(self.FORMS)
        self.click_element(self.PRACTICE_FORM)
        self.enter_text(self.FIRST_NAME,first_name)
        self.enter_text(self.LAST_NAME,last_name)
        self.enter_text(self.EMAIL,email)
        self.click_element(self.fill_gender_options(gender))
        self.enter_text(self.MOBILE,mobile)

        # Date of birth is entered using ActionChains
        actions=ActionChains(self.driver)
        date_input=self.find_element(self.DOB)
        date_input.send_keys(Keys.CONTROL + "a")
        date_input.send_keys(Keys.DELETE)
        actions.move_to_element(date_input).click().send_keys(dob).perform()

        # List of subjects are present and necessary data is typed
        subject_input=self.find_element(self.SUBJECTS)
        subject_input.send_keys(subject)
        subject_input.send_keys(Keys.ENTER)

        # To fill hobby,address and state
        self.click_element(self.fill_hobbies_options(hobby))
        self.enter_text(self.ADDRESS,address)
        self.click_element(self.STATE)
        self.click_element(self.fill_state(state))

        # To fill the city and click submit after entering all the details
        self.wait_for_element(self.CITY)
        city_input = self.find_element(self.CITY)
        city_input.send_keys(city)
        city_input.send_keys(Keys.ENTER)
        self.click_element(self.SUBMIT)




