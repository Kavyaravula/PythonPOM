from Config.testdata import TestData
from Pages.HomePage import HomePage
from Pages.LoginPage import LoginPage
from TestPages.TestBase import TestBase
import pytest


class TestHomePage(TestBase):

    def test_home_page_title(self):
        self.loginpage = LoginPage(self.driver)
        homepage = self.loginpage.do_login(TestData.USERNAME, TestData.PASSWORD)
        actual_title = homepage.get_home_page_title()
        assert actual_title == TestData.HOME_PAGE_TITLE

    def test_home_page_welcome_text(self):
        self.loginpage = LoginPage(self.driver)
        homepage = self.loginpage.do_login(TestData.USERNAME, TestData.PASSWORD)
        welcome_text = homepage.get_welcome_name_text()
        assert "Welcome" in welcome_text

    def test_home_page_tabs(self):
        self.loginpage = LoginPage(self.driver)
        homepage = self.loginpage.do_login(TestData.USERNAME, TestData.PASSWORD)
        actual_tabs = homepage.get_home_page_tab_names()
        assert actual_tabs == TestData.HOME_PAGE_TABS

    def test_home_page_subscribe_is_available(self):
        self.loginpage = LoginPage(self.driver)
        homepage = self.loginpage.do_login(TestData.USERNAME, TestData.PASSWORD)
        assert homepage.is_subscribe_available()

    def test_home_page_header_text(self):
        self.loginpage = LoginPage(self.driver)
        homepage = self.loginpage.do_login(TestData.USERNAME, TestData.PASSWORD)
        header_text = homepage.get_header_name()
        assert header_text == TestData.HOME_HEADER_NAME







