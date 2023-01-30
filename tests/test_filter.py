import pytest

from pages.main_page import MainPage


@pytest.mark.regression
def test_amy(browser):
    link = 'http://34.141.58.52:8080/#/'
    page = MainPage(browser, link)
    page.open()
    page.go_to_amy()
    browser.save_screenshot('filterAMY.png')


@pytest.mark.regression
def test_dori(browser):
    link = 'http://34.141.58.52:8080/#/'
    page = MainPage(browser, link)
    page.open()
    page.go_to_dori()
    browser.save_screenshot('filterDori.png')
