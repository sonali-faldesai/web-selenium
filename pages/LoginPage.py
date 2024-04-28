from data.locators import *
from utilities.selenium_base import SeleniumBaseMethods

class LoginPage():
    
    def __init__(self, driver) -> None:
        self.selenium_base_methods = SeleniumBaseMethods(driver)

    def enter_username(self, username):
        self.selenium_base_methods.enter_text(locator=username_xpath, text_to_enter=username)

    def enter_password(self, password):
        self.selenium_base_methods.enter_text(locator=password_xpath, text_to_enter=password)

    def click_login(self):
        self.selenium_base_methods.click(locator=login_btn_xpath)
