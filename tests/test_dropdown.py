import pytest
from pages.main_page import MainPage


@pytest.mark.regression
def test_go_to_dropdown(browser):
    link = 'http://34.141.58.52:8080/#/'
    page = MainPage(browser, link)
    page.open()
    page.go_to_dropdown()


@pytest.mark.regression
def test_dog_dropdown(browser):
    link = 'http://34.141.58.52:8080/#/'
    page = MainPage(browser, link)
    page.open()
    page.dog_dropdown()
    browser.save_screenshot('dog.png')


@pytest.mark.xfail
def test_reptile_dropdown(browser):
    link = 'http://34.141.58.52:8080/#/'
    page = MainPage(browser, link)
    page.open()
    page.reptile_dropdown()
    browser.save_screenshot('reptile.png')


def test_hamster_dropdown(browser):
    link = 'http://34.141.58.52:8080/#/'
    page = MainPage(browser, link)
    page.open()
    page.hamster_dropdown()
    browser.save_screenshot('hamster.png')
