import pytest
from selenium import webdriver
import unittest
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager


@pytest.mark.usefixtures("setup")
class Base(unittest.TestCase):
    pass

    # @pytest.fixture(scope='session')
    # def web_driver(self, request):
    #     driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    #     #driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
    #     request.cls.driver = driver
    #     driver.maximize_window()
    #     yield
    #     driver.close()

    @pytest.fixture(scope="class")
    def setup(self, request):
        print("initiating chrome driver")
        #driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
        driver.maximize_window()
        request.cls.driver = driver

        yield driver
        driver.close()




