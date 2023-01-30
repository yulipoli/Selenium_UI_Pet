import pytest
from tests.test_login import test_go_to_login_page
from pages.main_page import MainPage


@pytest.mark.smoke
def test_new_comment(browser):
    test_go_to_login_page(browser)
    link = 'http://34.141.58.52:8080/#/profile'
    page = MainPage(browser, link)
    page.open()
    page.new_comment()
    browser.save_screenshot('test1.png')