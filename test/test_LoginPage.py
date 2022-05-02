import time
import pytest
from src.LoginPage import LoginPage
from config.configs import TestData
from test.confest import Base
from src.SettingPage import SettingPage
from src.Profile_Page import ProfilePage


class Test_Login(Base):

    @pytest.mark.usefixtures("setup")
    def test_first_login_button(self):
        self.LoginPage = LoginPage(self.driver)
        self.LoginPage.first_login_button()
        self.LoginPage.do_login(TestData.user_name, TestData.password)

    @pytest.mark.usefixtures("setup")
    def test_setting_page(self):
        self.SettingPage_changes = SettingPage(self.driver)
        self.SettingPage_changes.setting_button()
        self.SettingPage_changes.profile_button()
        time.sleep(5)
        # self.SettingPage_changes.edit_name()
        # self.SettingPage_changes.change_user_name()
        # self.SettingPage_changes.save_update()

    @pytest.mark.usefixtures("setup")
    def test_profile_page(self):
        time.sleep(5)
        self.Profile_page_changes = ProfilePage(self.driver)
        time.sleep(5)
        self.Profile_page_changes.edit_name()
        # time.sleep(5)
        self.Profile_page_changes.change_user_name()
        time.sleep(5)
        self.Profile_page_changes.save_update()
        time.sleep(5)

