# Alerts,Frames,Windows Page for DEMO QA
# Importing By classes from selenium for locators
from selenium.webdriver.common.by import By
# To use the methods from base_page importing Class BasePage.
from Pages.base_page import BasePage


#AlertsPage inherits BasePage. AlertsPage contains locators to be used in test cases.
class AlertsPage(BasePage):

    # LOCATORS - Uses find_element() from BasePage to locate these elements while doing interactions.
    # Browser Windows locators using XPATH and ID
    ALERTS = (By.XPATH, '(//div[@class="category-cards"]//h5)[3]')
    BROWSER_WINDOW= (By.XPATH, '//span[text()="Browser Windows"]')
    TAB=(By.ID,'tabButton')
    TAB_HEADING=(By.ID,'sampleHeading')
    WINDOW=(By.ID,'windowButton')
    WINDOW_MESSAGE=(By.ID,'messageWindowButton')

    # Alerts button locators using XPATH and ID
    ALERT_TAB=(By.XPATH, '//span[text()="Alerts"]')
    ALERT_BUTTON=(By.ID,'alertButton')
    TIMER_ALERT=(By.ID,'timerAlertButton')
    CONFIRM_BUTTON=(By.ID,'confirmButton')
    CONFIRM_BUTTON_TEXT=(By.ID,'confirmResult')
    PROMPT_BUTTON=(By.ID,'promtButton')
    PROMPT_BUTTON_TEXT=(By.ID,'promptResult')

    # Frames locators
    FRAMES = (By.XPATH, '//span[text()="Frames"]')
    FRAME1=(By.ID,'frame1')
    FRAME2=(By.ID,'frame2')
    PAGE_TEXT=(By.XPATH, '//h1[@class="text-center"]')

    # Nested Frames locators
    NESTED_FRAMES = (By.XPATH, '//span[text()="Nested Frames"]')
    PARENT_FRAME=(By.ID,'frame1')
    CHILD_FRAME=(By.TAG_NAME,'iframe')
    INVALID_FRAME=(By.ID,'forms')
    TEXT=(By.XPATH,'//h1[text()="Nested Frames"]')


    # METHODS TO INTERACT WITH THE ELEMENTS
    # browser_windows() is used to switch between windows
    def browser_windows(self):
        self.click_element(self.ALERTS)
        self.click_element(self.BROWSER_WINDOW)

        # parent stores the current window
        parent = self.driver.current_window_handle

        # 3 different windows
        self.click_element(self.TAB)
        self.click_element(self.WINDOW)
        self.click_element(self.WINDOW_MESSAGE)

        # handles contains all the different windows.
        handles = self.driver.window_handles
        for handle in handles:
            if handle != parent:
                # Used to switch between different windows[driver.switch_to.window(window_name)]
                self.driver.switch_to.window(handle)
                break


    # alert_button() is used to click the alert button and clicks the ok button in the alert message
    def alert_button(self):
        self.click_element(self.ALERTS)
        self.click_element(self.ALERT_TAB)
        self.click_element(self.ALERT_BUTTON)
        # accept() refers to clicking the ok button
        self.driver.switch_to.alert.accept()


    # no alert_button() is used to click the invalid alert button
    def no_alert_button(self):
        self.click_element(self.ALERTS)
        self.click_element(self.ALERT_TAB)
        # accept() refers to clicking the ok button
        self.driver.switch_to.alert.accept()


    # timer_alert_button() clicks the timer alert which appears after 0.5 secs
    def timer_alert_button(self):
        self.click_element(self.ALERTS)
        self.click_element(self.ALERT_TAB)
        self.click_element(self.TIMER_ALERT)
        self.wait_for_alert()


    # confirm_alert_button() clicks the confirm alert either to click OK or Cancel
    def confirm_alert_button(self):
        self.click_element(self.ALERTS)
        self.click_element(self.ALERT_TAB)
        self.click_element(self.CONFIRM_BUTTON)

        # accept() clicks OK and dismiss clicks CANCEL
        self.driver.switch_to.alert.dismiss()


    # prompt_alert_button() opens a prompt where name is entered in text box and clicks OK
    def prompt_alert_button(self,name):
        self.click_element(self.ALERTS)
        self.click_element(self.ALERT_TAB)
        self.click_element(self.PROMPT_BUTTON)
        self.driver.switch_to.alert.send_keys(name)
        self.driver.switch_to.alert.accept()


    # frames() is used to switch between 2 different frames
    def frames(self):
        self.click_element(self.ALERTS)
        self.click_element(self.FRAMES)
        self.driver.switch_to.frame(self.find_element(self.FRAME1))
        self.driver.switch_to.default_content()

        # Switches to main page before switching to next frame
        self.driver.switch_to.frame(self.find_element(self.FRAME2))
        self.driver.switch_to.default_content()
        self.find_element(self.PAGE_TEXT)


    # nested_frames() is used to switch between parent and child frame
    def nested_frames(self):
        self.click_element(self.ALERTS)
        self.click_element(self.NESTED_FRAMES)
        self.driver.switch_to.frame(self.find_element(self.PARENT_FRAME))

        self.driver.switch_to.frame(self.find_element(self.CHILD_FRAME))
        self.driver.switch_to.default_content()
        self.find_element(self.TEXT)


    # invalid_frame() is used to switch between parent and invalid child frame
    def invalid_frame(self):
        self.click_element(self.ALERTS)
        self.click_element(self.NESTED_FRAMES)
        self.driver.switch_to.frame(self.find_element(self.PARENT_FRAME))
        self.driver.switch_to.frame("CHILD_FRAME")





