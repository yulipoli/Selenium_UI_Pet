import pytest

from tests.test_login import test_go_to_login_page
from pages.profile_page import ProfilePage


@pytest.mark.regression
def test_new_pet_creation(browser):
    test_go_to_login_page(browser)
    link = 'http://34.141.58.52:8080/#/profile'
    page = ProfilePage(browser, link)
    page.open()
    page.create_new_pet_dori()
    page.create_new_pet_amy()
