# Test Classes contains test scripts and calling actions
# Importing pytest modules to use in test cases
import pytest
# Importing Alerts page to use methods in it.
from Pages.alerts_page import AlertsPage
# Importing necessary data from Utils to be used
from Utils.utils import name


#To use setup fixture from conftest.py
@pytest.mark.usefixtures("setup")
class TestAlertButtons:

    # test_switch_windows() switches between different child windows and parent window
    @pytest.mark.positive
    def test_switch_windows(self):
        #This line creates an instance of the AlertsPage class, and passes the WebDriver instance (self.driver) to it.
        alerts=AlertsPage(self.driver)
        alerts.browser_windows()
        assert "https://demoqa.com/sample" in alerts.get_current_url()


    # test_alert_button() clicks the button to see the alert and clicks ok[Accepts the alert]
    @pytest.mark.positive
    def test_alert_button(self):
        alert_prompts = AlertsPage(self.driver)
        alert_prompts.alert_button()


    # test_no_alert_button() clicks the invalid alert button and throws NoAlertPresentException
    @pytest.mark.negative
    def test_no_alert_button(self):
        alert_prompts = AlertsPage(self.driver)
        alert_prompts.no_alert_button()


    # test_timer_alert() clicks the button to see the alert which appears after 5 seconds
    @pytest.mark.positive
    def test_timer_alert(self):
        timer_alert=AlertsPage(self.driver)
        timer_alert.timer_alert_button()


    # test_confirm_alert() clicks the confirm button and ok or cancel can be clicked
    # Prints whether ok or cancel is clicked
    @pytest.mark.positive
    def test_confirm_alert(self):
        confirm_alert=AlertsPage(self.driver)
        confirm_alert.confirm_alert_button()
        alert_text=confirm_alert.find_element(confirm_alert.CONFIRM_BUTTON_TEXT).text
        assert "You selected Cancel" in alert_text
        print(f"{alert_text}")


    # test_prompt_alert() opens a prompt box and data is entered and submitted
    # Accept or Dismiss can be done in this prompt box
    @pytest.mark.positive
    def test_prompt_alert(self):
        prompt_alert=AlertsPage(self.driver)
        prompt_alert.prompt_alert_button(name)
        prompt_text=prompt_alert.find_element(prompt_alert.PROMPT_BUTTON_TEXT).text
        assert "Ujjaini" in prompt_text


    # test_alert_with_invalid_data() opens a prompt box and invalid data is entered and submitted
    # Accept or Dismiss can be done in this prompt box and this throws Assertion Error
    @pytest.mark.negative
    def test_alert_with_invalid_data(self):
        prompt_alert=AlertsPage(self.driver)
        prompt_alert.prompt_alert_button(name)
        prompt_text=prompt_alert.find_element(prompt_alert.PROMPT_BUTTON_TEXT).text
        assert "Diya" in prompt_text

