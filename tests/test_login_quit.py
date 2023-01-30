import pytest

from tests.test_login import test_go_to_login_page
from pages.login_page import LoginPage


@pytest.mark.regression
def test_login_quit(browser):
    test_go_to_login_page(browser)
    link = 'http://34.141.58.52:8080/#/profile'
    page = LoginPage(browser, link)
    page.open()
    page.login_quit()
