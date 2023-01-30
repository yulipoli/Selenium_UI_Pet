import pytest

from pages.login_page import LoginPage


@pytest.mark.regression
def test_go_to_login(browser, login_email=None):
    link = 'http://34.141.58.52:8080/#/login'
    page = LoginPage(browser, link)
    page.open()
    page.go_to_login()
    assert login_email != 0


@pytest.mark.regression
def test_input_password(browser):
    link = 'http://34.141.58.52:8080/#/login'
    page = LoginPage(browser, link)
    page.open()
    page.test_input_password()


@pytest.mark.regression
def test_submit_button(browser):
    link = 'http://34.141.58.52:8080/#/login'
    page = LoginPage(browser, link)
    page.open()
    page.test_submit_button()
