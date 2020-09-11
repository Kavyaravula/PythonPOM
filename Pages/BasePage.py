from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import Select



class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def do_send_keys(self, by_locator, text):
        WebDriverWait(self.driver, 15).until(EC.visibility_of_element_located(by_locator)).send_keys(text)

    def do_clcik(self, by_locator):
        WebDriverWait(self.driver, 15).until(EC.visibility_of_element_located(by_locator)).click()

    def get_element_text(self, by_locator):
        element = WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located(by_locator))
        return element.text

    def is_element_visible(self, by_locator):
        element = WebDriverWait(self.driver, 15).until(EC.visibility_of_element_located(by_locator))
        return bool(element)

    def get_title(self):
        return self.driver.title

    def do_select_dropdown_visible_text(self, by_locator, text):
        element = WebDriverWait(self.driver, 15).until(EC.visibility_of_element_located(by_locator))
        select = Select(element)
        select.select_by_visible_text(text)

    def do_select_checkbox(self, by_locator):
        WebDriverWait(self.driver, 15).until(EC.visibility_of_element_located(by_locator)).click()

    def do_mouse_over(self, by_locator):
        element = WebDriverWait(self.driver, 15).until(EC.visibility_of_element_located(by_locator))
        ActionChains(self.driver).move_to_element(element).perform()

    def do_get_elements_text(self, by_locator):
        elements = WebDriverWait(self.driver,20).until(EC.visibility_of_all_elements_located(by_locator))
        actual_elements_text = []
        for element in elements:
            actual_elements_text.append(element.text)
        return actual_elements_text











