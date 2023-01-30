import pytest

from tests.test_login import test_go_to_login_page
from pages.profile_page import ProfilePage


@pytest.mark.smoke
def test_edit_pet(browser):
    test_go_to_login_page(browser)
    link = 'http://34.141.58.52:8080/#/profile'
    page = ProfilePage(browser, link)
    page.open()
    page.edit_pet()