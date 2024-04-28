from data.locators import *
from utilities.selenium_base import SeleniumBaseMethods

class HomePage():
    
    def __init__(self, driver) -> None:
        self.selenium_base_methods = SeleniumBaseMethods(driver)

    def get_homepage_title(self):
        return self.selenium_base_methods.get_title()