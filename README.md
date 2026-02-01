                             ** Automation Testing of DEMO QA(https://demoqa.com/) **

This project automates the testing of the web application (https://demoqa.com/) by simulating user actions and validating its core functionalities. The key modules covered include login, menu accessibility,elements[Textbox,Checkbox,Radio button],buttons,upload,download,forms,switching windows,frames,alerts,tables. It ensures the reliability of critical components through both positive and negative test scenarios.

The test scripts are developed using Selenium with Python and Pytest, following the Page Object Model (POM) framework and adhering to Object-Oriented Programming (OOP) principles. The test data is externalized (CSV) using Data Driven framework, and common configurations are handled in config.py.The suite includes 14 detailed test cases focused on verifying page behavior, accessibility of essential elements, navigation flows, and login processes.


**Project Architecture :**

**MiniProject2/**
│
├── **Data/**
│   ├── __init__.py
│   ├── invalid_login_data.csv
├── **Pages/**
│   ├── __init__.py
│   ├── alerts_page.py
│   ├── base_page.py
│   ├── books_page.py
│   ├── demo_page.py
│   ├── element_page.py
│   ├── forms_page.py
│
├── **Tests/**
│   ├── __init__.py
│   ├── conftest.py
│   ├── test_01_homeURL.py
│   ├── test_02_title.py
│   ├── test_03_menu_visibility.py
│   ├── test_04_textbox.py
│   ├── test_05_checkbox_radio.py
│   ├── test_06_webtable.py
│   ├── test_07_mouse_events.py
│   ├── test_08_upload_download.py
│   ├── test_09_practice_form.py
│   ├── test_10_alerts.py
│   ├── test_11_frames.py
│   ├── test_12_book_login.py
│   ├── test_13_multiple_login.py
│   ├── test_14_book_store_table.py
│
├── **Utils/**
│   ├── __init__.py
│   ├── config.py
│
├── requirements.txt
├── README.md



**Tools & Technologies:**
*     Selenium WebDriver
*     Python 
*     Pytest
*     OOPS
*     Page Object Model (POM)
*     Data Driven Testing
*     Test Data(CSV file)
*     Explicit Waits
*     Exception Handling
*     Pytest HTML Reports


  **Test Suite :**

  Test Case 1: Verify that the home URL is accessible

	* Positive case: Validates proper navigation to (https://demoqa.com/) and asserts current URL
	* Negative case: Invalid URL navigation and displays error message

   Test Case 2: Verify that page title of demo page

	* Positive case: Validates the page title matches or not
	* Negative case: Invalid page title and displays error message

   Test Case 3: Checks visibility and clickability of menu items 

	* Positive case: Validate menu items stored as dictionary are visible and interactable 
	* Negative case: Invalid access to menu items throws error message

   Test Case 4: Validation of name,email,address using Textbox

	* Positive case: Validates by entering details and checks the submitted data
	* Negative case: Textbox is filled with single quotes for all the textbox and it throws Assertion Error

   Test Case 5: Validate of Checkbox and Radio button
  
	* Positive case: Selects the Home Checkbox and displays the message.Selects the radio button[Yes,Impressive,No] and displays the message
	* Negative case: Doesn't selects Home Checkbox,radio button and throws TimeoutException

   Test Case 6: Displays that web table of demo page

	* Positive case: Prints the web table of page which includes details like Firstname,Lastname,Age,Email,Salary,Department
	* Negative case:

   Test Case 7: Validates the mouse events using ActionChains

	* Positive case: Validates the mouse events like double click, right click and click using  ActionChains
	* Negative case: Performs invalid click on button and using pytest raises TimeoutException and test succeeds

   Test Case 8: Validates the file upload functionality

	* Positive case: Validates file upload and asserts the file path
	* Negative case: Downloads the file from demo page and stores under Tests folder

    Test Case 9: Validates the Practice Form

	* Positive case: Enter valid text into input fields (Name,Email,Gender,DOB,Subjects,Hobbies,State and City,.) and verify input is accepted
	* Negative case: Provides invalid data in City field and this throws ElementClickInterceptedException

    Test Case 10: Verify the demo page alerts and switching windows

	* Positive case: Validates the switching windows between 3 different winodws. Performs 4 different alerts like clicking button to see alert,accepting 				alert,dismiss alert and to send data and accept the alert.
	* Negative case: Clicks the invalid alert button and it throws NoAlertPresentException.Enters an invalid data in alert box and checks with some other data 			which throws Assertion Error.

    Test Case 11: Validates the frames and nested frames of demo oage

	* Positive case: Validates switches between different frames and switches back to page and asserts the data in main page.Validates switches between parent 			and child frame in a nested frame
	* Negative case: Perfroms switches between valid and an invalid frame,throws NoSuchFrameException

   Test Case 12: Validates the Book Store Login Functionality

	* Registers new user to book store which includes details like Firstname,Lastname,Username and password and asserts the URL
	* Logins with newly created username and password and asserts the credentials.

    Test Case 13: Validates login functionality with different invalid credentials using external CSV file

	* Login with invalid credentials and displays the error message

	Test Case 14: Validates book store of book store application

 	* Displays the book details in table format[Book Title,Image,Publisher]
    * Searches the necessary book/title/publisher using Search box and asserts the data



Instructions:

1.Ensure Selenium,Python and any Browser(Chrome,Firefox,Edge) installed in your system.

2.To create a virtual environment,

>python -m venv venv

>source venv/bin/activate(macOS)

>venv\scripts\activate(Windows)

3.To install the dependencies,

>pip install -r requirements.txt

4.To execute all the test files,

>pytest -v -s Tests/

>pytest pytest -v -s Tests/ttest_01_homeURL.py(for any specific file)

>pytest pytest -v -s Tests/test_01_homeURL.py::test_valid_url(for specific method in a test file)


To Generate HTML Report:

To install pytest–html package

>pip install pytest–html

To execute all the test files and generate html report,

>pytest -v -s Tests/   --html=reports.html    --self-contained-html

To execute single file and generate html report,

>pytest -v -s Tests/test_01_homeURL.py --html=case01_report.html   --self-contained-html

   

   
