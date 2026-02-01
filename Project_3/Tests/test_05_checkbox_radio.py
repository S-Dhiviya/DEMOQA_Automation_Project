# Test Classes contains test scripts and calling actions
# Importing pytest modules to use in test cases
import pytest
# Importing element page to use methods in it.
from Pages.element_page import ElementPage
# Importing necessary data from Utils to be used
from Utils.utils import radio_button_option


#To use setup fixture from conftest.py
@pytest.mark.usefixtures("setup")
class TestCheckboxRadio:

    # test_checkbox_validation() ensures Home button is checked and content is displayed
    @pytest.mark.positive
    def test_checkbox_validation(self):
        #This line creates an instance of the ElementPage class, and passes the WebDriver instance (self.driver) to it.
        element=ElementPage(self.driver)
        element.check_box()


    #  test_invalid_checkbox() ensures Home button is unchecked and throws TimeoutException
    @pytest.mark.negative
    def test_invalid_checkbox(self):
        # This line creates an instance of the ElementPage class, and passes the WebDriver instance (self.driver) to it.
        element = ElementPage(self.driver)
        element.invalid_check_box()


    # test_radiobutton_validation() selects the necessary radio button and prints the radio option
    #Radio button[ 1-yes 2-Impressive 3-No]
    @pytest.mark.positive
    def test_radiobutton_validation(self):
        element = ElementPage(self.driver)
        element.radio_button(radio_button_option)


   # test_invalid_radiobutton() searches the necessary radio button and throws the error
    @pytest.mark.negative
    def test_invalid_radiobutton(self):
        element = ElementPage(self.driver)
        element.invalid_radio_button(radio_button_option)

    


