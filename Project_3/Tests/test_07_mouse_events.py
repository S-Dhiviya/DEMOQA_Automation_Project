# Test Classes contains test scripts and calling actions
# Importing pytest modules to use in test cases
import pytest
# Importing element page to use methods in it.
from Pages.element_page import ElementPage
from selenium.common import TimeoutException


#To use setup fixture from conftest.py
@pytest.mark.usefixtures("setup")
class TestMouseEvents:

    # test_mouse_events() performs different mouse events like click,double click and right click
    @pytest.mark.positive
    def test_mouse_events(self):
        # This line creates an instance of the ElementPage class, and passes the WebDriver instance (self.driver) to it.
        element = ElementPage(self.driver)
        element.buttons()
        assert "You have done a double click" in element.find_element(element.DOUBLE_CLICK_TEXT).text


    #  test_invalid_mouse_click() performs invalid clicks on buttons and throws TimeoutException
    # This negative case passes because it raises TimeoutException
    @pytest.mark.negative
    def test_invalid_mouse_click(self):
        element = ElementPage(self.driver)
        element.invalid_click_on_buttons()
        with pytest.raises(TimeoutException):
            assert "You have done a double click" in element.find_element(element.DOUBLE_CLICK_TEXT).text




