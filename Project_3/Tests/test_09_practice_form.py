# Test Classes contains test scripts and calling actions
# Importing pytest modules to use in test cases
import pytest
# Importing Forms page to use methods in it.
from Pages.forms_page import FormsPage
# Importing necessary data from Utils to be used
from Utils.utils import *


#To use setup fixture from conftest.py
@pytest.mark.usefixtures("setup")
class TestForm:

    # test_practice_form() fills the data in Student Registration Form like [Name,Age,Gender,Subject,..]
    @pytest.mark.positive
    def test_practice_form(self):
        #This line creates an instance of the FormsPage class, and passes the WebDriver instance (self.driver) to it.
        forms=FormsPage(self.driver)
        forms.student_form(first_name,last_name,email,gender,mobile,DOB,subject,hobby,address,state,city)


    # test_invalid_data_form() fills the invalid data in Student Registration Form like [Name,Age,Gender,Subject,..]
    # This throws ElementClickInterceptedException since City value is invalid
    @pytest.mark.negative
    def test_invalid_data_form(self):
        #This line creates an instance of the FormsPage class, and passes the WebDriver instance (self.driver) to it.
        forms=FormsPage(self.driver)
        forms.student_form(first_name,last_name,email,gender,mobile,DOB,subject,hobby,address,state,city='Chennai')

