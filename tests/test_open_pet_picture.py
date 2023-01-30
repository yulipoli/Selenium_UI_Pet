import pytest

from tests.test_login import test_go_to_login_page
from pages.main_page import MainPage


@pytest.mark.regression
def test_open_pet_picture(browser):
    test_go_to_login_page(browser)
    link = 'http://34.141.58.52:8080/#/profile'
    page = MainPage(browser, link)
    page.open()
    page.open_pet_picture()