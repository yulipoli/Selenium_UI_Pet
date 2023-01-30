import time

from .base_page import BasePage
from locators.locator import LoginPageLocators


class LoginPage(BasePage):
    def go_to_login_page(self):
        login_email = self.browser.find_element(*LoginPageLocators.LOGIN_EMAIL)
        login_email.send_keys('yulia@gmail.com')
        login_pass = self.browser.find_element(*LoginPageLocators.LOGIN_PASS)
        login_pass.send_keys("yulia")
        login_btn = self.browser.find_element(*LoginPageLocators.LOGIN_BTN)
        login_btn.submit()

    def login_quit(self):
        quit_btn = self.browser.find_element(*LoginPageLocators.QUIT_BTN)
        quit_btn.click()
        time.sleep(2)

    def go_to_login(self):
        login_email = self.browser.find_element(*LoginPageLocators.LOGIN_EMAIL)
        login_email.send_keys('yulia@gmail.com')
        return login_email

    def test_input_password(self):
        login_pass = self.browser.find_element(*LoginPageLocators.LOGIN_PASS)
        login_pass.send_keys("yulia")

    def test_submit_button(self):
        login_btn = self.browser.find_element(*LoginPageLocators.LOGIN_BTN)
        login_btn.submit()
