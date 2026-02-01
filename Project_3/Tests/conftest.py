# conftest.py is used to define fixtures that can be reused across multiple test files.
#To import pytest modules
import pytest
#Importing Webdriver module from Selenium library
from selenium import webdriver
# Importing ChromeDriverManager and Service from Selenium library
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
# Importing Options from Selenium library
from selenium.webdriver.chrome.options import Options


# Fixtures are functions in pytest used to prepare environment for test execution.Scope by default it is "function".
#Scope="class" defines set up and tear down for each class
@pytest.fixture(scope="function")
# request is a built-in pytest fixture that gives you access to the test context. setup is fixture name
def setup(request):

    # Options to set the desired capabilities like download path,prompt to be FALSE
    options = Options()
    options.add_argument('--disable-notifications')
    prefs = {
        "download.default_directory": "/Users/dhiviya/Documents/Mini3/Tests",
        "download.prompt_for_download": False,
        "safebrowsing.enabled": True
    }
    options.add_experimental_option("prefs", prefs)
    # Creates Webdriver instance
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

    # get() navigates to DEMO QA portal and opens in Chrome Browser
    driver.get("https://demoqa.com/")
    #This is used to view the Chrome Browser in maximized window
    driver.maximize_window()

    # request.cls.driver = driver lets self.driver to be used inside test class methods.
    request.cls.driver =driver
    # yield is used for setup and teardown logic
    yield
    # Closes the Chrome Window and ends the WebDriver session
    driver.quit()