import time
from selenium.webdriver.common.by import By


class SeleniumBaseMethods():
    def __init__(self, driver) -> None:
        self.driver = driver

    def enter_text(self, locator, text_to_enter):
        element = self.driver.find_element(by=By.XPATH, value=locator)
        element.clear()
        element.send_keys(text_to_enter)

    def click(self, locator):
        element = self.driver.find_element(by=By.XPATH, value=locator)
        element.click()

    def get_title(self):
        return self.driver.title

    def clean_up(self):
        time.sleep(10)
        self.driver.quit()
