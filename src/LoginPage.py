import time

from src.BasePage import BasePage
from selenium.webdriver.common.by import By
from config.configs import TestData
from src.SettingPage import SettingPage


class LoginPage(BasePage):

    click_login = (By.XPATH, "//*[text()='Log In']")
    email = (By.XPATH, "//*[@name ='email' ]")
    pwd = (By.XPATH, "//*[@name ='password' ]")
    login_btn = (By.XPATH, "//div//button[text()='Log in']")
    signup_link = (By.LINK_TEXT, "Sign up")

    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get(TestData.base_url)

    def get_login_page_title(self, title):
        return self.get_title(title)

    def is_signup_link(self, ):
        return self.is_visible(self.signup_link)

    def first_login_button(self):
        return self.click_method(self.click_login)

    def do_login(self, username, password):
        self.send_keys_method(self.email, username)
        self.send_keys_method(self.pwd, password)
        self.click_method(self.login_btn)
        # This time has been added since it's speed is ver fast.
        #time.sleep(5)
        #return SettingPage(self.driver)


