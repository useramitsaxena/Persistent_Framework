from src.BasePage import BasePage
from selenium.webdriver.common.by import By
from config.configs import TestData
from src.Profile_Page import ProfilePage


class SettingPage(BasePage):

    setting_btn = (By.XPATH, "//div[text()='Settings']")
    profile = (By.XPATH, "//*[text()='Profile']")
    user_name = (By.XPATH, "//*[@id='user_name']")
    save_changes = (By.XPATH, "//*[text()='Update Preferences']")


    def __init__(self, driver):
        super().__init__(driver)

    def setting_button(self):
        return self.click_method(self.setting_btn)

    def profile_button(self):
        return self.click_method(self.profile)
        #return ProfilePage(self.driver)

    def click_profile_name(self):
        return self.click_method(self.user_name)

    def edit_name(self):
        return self.clear_text(self.user_name)

    def change_user_name(self):
        return self.send_keys_method(self.user_name, TestData.new_name)

    def save_update(self):
      return self.click_method(self.save_changes)



