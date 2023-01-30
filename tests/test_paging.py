import pytest

from pages.main_page import MainPage
from tests.test_login import test_go_to_login_page


@pytest.mark.smoke
def test_paging(browser):
    test_go_to_login_page(browser)
    link = 'http://34.141.58.52:8080/#/profile'
    page = MainPage(browser, link)
    page.open()
    page.paging()
