from data.locators import *
from utilities.selenium_base import SeleniumBaseMethods

class RegisterPage():
    
    def __init__(self, driver) -> None:
        self.selenium_base_methods = SeleniumBaseMethods(driver)

    def select_register_option(self):
        self.selenium_base_methods.click(locator="")
        