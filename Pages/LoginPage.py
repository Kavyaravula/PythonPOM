from selenium.webdriver.common.by import By

from Config.testdata import TestData
from Pages.BasePage import BasePage
from Pages.HomePage import HomePage


class LoginPage(BasePage):
    ''' By Locators -- object repository'''


    USER_NAME = (By.NAME, "txtUsername")
    PASSWORD = (By.NAME, "txtPassword")
    LOGIN_BUTTON = (By.NAME, "Submit")
    FORGOT_PASSWORD_LINK = (By.LINK_TEXT, "Forgot your password?")

    ''' Constructor of the page class'''

    def __init__(self, driver):
        super().__init__(driver)


    '''Page actions for login page'''

    def get_login_page_title(self):
        return self.get_title()

    def forgot_password_link_available(self):
        return self.is_element_visible(self.FORGOT_PASSWORD_LINK)

    def do_login(self, username, password):
        self.do_send_keys(self.USER_NAME, username)
        self.do_send_keys(self.PASSWORD, password)
        self.do_clcik(self.LOGIN_BUTTON)
        return HomePage(self.driver)









