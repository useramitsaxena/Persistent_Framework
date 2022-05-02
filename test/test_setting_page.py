import time

import pytest
# from test.test_base import BaseTest
from src.LoginPage import LoginPage
from config.configs import TestData
from test.confest import Base
from src.SettingPage import SettingPage
from src.Profile_Page import ProfilePage


class Test_Setting(Base):

    def test_setting_page(self):
        self.LoginPage = LoginPage(self.driver)
        self.LoginPage.first_login_button()
        self.SettingPage_changes = self.LoginPage.do_login(TestData.user_name, TestData.password)
        self.SettingPage_changes.setting_button()
        self.SettingPage_changes.profile_button()
        self.SettingPage_changes.edit_name()
        self.SettingPage_changes.change_user_name()
        self.SettingPage_changes.save_update()


    # def test_setting_pagesss(self):
    #     self.LoginPage = LoginPage(self.driver)
    #     self.LoginPage.first_login_button()
    #     SettingPage_changes = self.LoginPage.do_login(TestData.user_name, TestData.password)
    #     SettingPage_changes.setting_button()
    #     profile = SettingPage_changes.profile_button()
    #     profile.edit_name()
    #     profile.change_user_name()
    #     profile.save_update()
