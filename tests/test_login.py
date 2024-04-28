import time

import pytest
from pages.HomePage import HomePage
from pages.LoginPage import LoginPage
from data.constants import *


@pytest.mark.usefixtures("launch_app")
class TestLogin:

    def setup_method(self):
        self.login_page = LoginPage(self.driver)
        self.home_page = HomePage(self.driver)

    def test_login_with_valid_creds(self):
        self.login_page.enter_username(username)
        self.login_page.enter_password(password)
        time.sleep(2)
        self.login_page.click_login()

        assert self.home_page.get_homepage_title() == "ParaBank | Accounts Overview"

        