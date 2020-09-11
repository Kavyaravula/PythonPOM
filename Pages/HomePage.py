from selenium.webdriver.common.by import By

from Pages.BasePage import BasePage


class HomePage(BasePage):
    WELCOME_NAME = (By.ID, "welcome")
    SUBSCRIBE_LINK =(By.ID, "Subscriber_link")
    DASHBOARD_HEADER = (By.XPATH, "//h1[text()='Dashboard']")
    HOME_PAGE_TABS = (By.XPATH, "//li[contains(@class,'main-menu')]//b")

    def __init__(self, driver):
        super().__init__(driver)

    def get_home_page_title(self):
        return self.get_title()

    def get_welcome_name_text(self):
        return self.get_element_text(self.WELCOME_NAME)

    def is_subscribe_available(self):
        return self.is_element_visible(self.SUBSCRIBE_LINK)

    def get_header_name(self):
        return self.get_element_text(self.DASHBOARD_HEADER)

    def get_home_page_tab_names(self):
        return self.do_get_elements_text(self.HOME_PAGE_TABS)






