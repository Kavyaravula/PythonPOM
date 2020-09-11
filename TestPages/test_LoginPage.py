import pytest

from Config.testdata import TestData
from Pages.LoginPage import LoginPage
from TestPages.TestBase import TestBase


class TestLoginPage(TestBase):

    def test_login_page_title(self):
        self.loginpage = LoginPage(self.driver)
        actual_title = self.loginpage.get_login_page_title()
        assert actual_title == TestData.LOGIN_PAGE_TITLE

    def test_forgot_password_availability(self):
        self.loginpage = LoginPage(self.driver)
        flag = self.loginpage.forgot_password_link_available()
        assert flag

    def test_login_orange_hrm(self):
        self.loginpage = LoginPage(self.driver)
        self.loginpage.do_login(TestData.USERNAME, TestData.PASSWORD)


