# Test Classes contains test scripts and calling actions
# Importing pytest modules to use in test cases
import pytest
# Importing base page to use methods in it.
from Pages.base_page import BasePage
from Pages.alerts_page import AlertsPage


#To use setup fixture from conftest.py
@pytest.mark.usefixtures("setup")
class TestFrames:

    # test_frames() switches between different frames and switches back to page
    @pytest.mark.positive
    def test_frames(self):
        # This line creates an instance of the AlertsPage class, and passes the WebDriver instance (self.driver) to it.
        frame=AlertsPage(self.driver)
        frame.frames()
        assert "Frames" in frame.find_element(frame.PAGE_TEXT).text


    # test_nested_frames() switches between parent and child frame in a nested frame
    @pytest.mark.positive
    def test_nested_frames(self):
        # This line creates an instance of the AlertsPage class, and passes the WebDriver instance (self.driver) to it.
        nested_frame=AlertsPage(self.driver)
        nested_frame.nested_frames()
        assert "Nested Frames" in nested_frame.find_element(nested_frame.TEXT).text


    # test_invalid_frame() switches between valid and an invalid frame,throws NoSuchFrameException
    @pytest.mark.negative
    def test_invalid_frame(self):
        frames = AlertsPage(self.driver)
        frames.invalid_frame()