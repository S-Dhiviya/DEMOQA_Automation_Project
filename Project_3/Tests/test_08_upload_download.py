# Test Classes contains test scripts and calling actions
# Importing pytest modules to use in test cases
import pytest
# Importing element page to use methods in it.
from Pages.element_page import ElementPage


#To use setup fixture from conftest.py
@pytest.mark.usefixtures("setup")
class TestUploadDownload:

    # test_file_upload() uploads file from local path and asserts the file path
    @pytest.mark.positive
    def test_file_upload(self):
        # This line creates an instance of the ElementPage class, and passes the WebDriver instance (self.driver) to it.
        element = ElementPage(self.driver)
        element.upload_file()
        file_path=element.find_element(element.FILE_UPLOAD_PATH).text
        assert file_path=="C:\\fakepath\\myfile.txt"


    # test_file_download() downloads the file from the demo page and saves under Tests folder
    # Desired capabilities are given under conftest.py like download path
    @pytest.mark.positive
    def test_file_download(self):
        element = ElementPage(self.driver)
        element.click_element(element.ELEMENTS)
        element.click_element(element.UPLOAD)
        element.click_element(element.DOWNLOAD)

