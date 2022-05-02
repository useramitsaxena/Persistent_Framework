import time

from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

""" This is our Base Page Class"""


class BasePage:

    def __init__(self, driver):
        self.driver = driver

    def click_method(self, by_locator):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(by_locator)).click()

    def send_keys_method(self, by_locator, text):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator)).send_keys(text)

    def get_element(self, by_locator):
        ele = WebDriverWait(self.driver, 2).until(EC.visibility_of_element_located(by_locator))
        return ele.text

    def is_visible(self, by_locator):
        ele = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator))
        return bool(ele)

    def get_title(self,title):
        WebDriverWait(self.driver, 2).until(EC.title_is(title))
        return self.driver.title

    def clear_text(self, by_locator):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator)).clear()

