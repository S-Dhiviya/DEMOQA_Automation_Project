# Test Classes contains test scripts and calling actions
# Importing pytest modules to use in test cases
import pytest
# Importing element page to use methods in it.
from Pages.element_page import ElementPage
# Importing necessary data from Utils to be used
from Utils.utils import full_name,email,current_address,permanent_address


#To use setup fixture from conftest.py
@pytest.mark.usefixtures("setup")
class TestTextBox:

    # test_textbox_validation() checks whether all the details gets entered and submitted
    @pytest.mark.positive
    def test_textbox_validation(self):
        #This line creates an instance of the ElementPage class, and passes the WebDriver instance (self.driver) to it.
        element=ElementPage(self.driver)
        element.text_box(full_name,email,current_address,permanent_address)
        assert "https://demoqa.com/text-box" in element.get_current_url()
        assert "diya" in element.find_element(element.OUTPUT).text


    #test_textbox_invalid_input() checks whether output appears even when no text is entered
    # This throws assertion error
    @pytest.mark.negative
    def test_textbox_invalid_input(self):
        # This line creates an instance of the ElementPage class, and passes the WebDriver instance (self.driver) to it.
        element = ElementPage(self.driver)
        element.text_box('','','','')
        assert not element.find_element(element.OUTPUT)







