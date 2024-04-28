import pytest
from data.constants import *
from pages.RegisterPage import RegisterPage


@pytest.mark.usefixtures("launch_app")
class TestRegister:

    def setup_method(self):
        self.register_page = RegisterPage(self.driver)

    def test_register_with_valid_data(self):
        pass
