import sys
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

sys.path.append("C:\\Users\\jasmeetsingh59\\Documents\\PracticeTest\\ParaBankAppAutomation")
from data.constants import *


@pytest.fixture(scope="class")
def launch_app(request):
    
    driver = webdriver.Chrome(service=Service(executable_path=ChromeDriverManager().install()))
    driver.get(app_url)
    driver.maximize_window()
    request.cls.driver = driver
    yield
