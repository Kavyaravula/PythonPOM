import pytest
from selenium import webdriver
from selenium.webdriver import Chrome
from selenium.webdriver import Firefox
from selenium.webdriver import Edge
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager

from Config.testdata import TestData


@pytest.fixture(params=["chrome"])
def init_browser_and_tear_down(request):
    if request.param == "chrome":
        driver = webdriver.Chrome(ChromeDriverManager().install())

    elif request.param == "firefox":
        driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
    elif request.param == "edge":
        driver = webdriver.Edge(EdgeChromiumDriverManager().install())
    driver.maximize_window()
    driver.get(TestData.BASE_URL)
    request.cls.driver = driver

    yield
    driver.quit()


