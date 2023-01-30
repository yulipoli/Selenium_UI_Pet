import time

from locators.locator import MainPageLocators
from .base_page import BasePage


class MainPage(BasePage):
    def go_to_login_page(self):
        login_link = self.browser.find_element(*MainPageLocators.LOGIN_LINK)
        login_link.click()

    def paging(self):
        logo = self.browser.find_element(*MainPageLocators.LOGO)
        logo.click()
        second_p = self.browser.find_element(*MainPageLocators.SECOND_P)
        time.sleep(2)
        second_p.click()
        time.sleep(2)
        third_p = self.browser.find_element(*MainPageLocators.THIRD_P)
        third_p.click()
        time.sleep(2)
        last_p = self.browser.find_element(*MainPageLocators.LAST_P)
        last_p.click()
        time.sleep(2)
        previous_p = self.browser.find_element(*MainPageLocators.PREVIOUS_P)
        previous_p.click()
        time.sleep(2)
        next_p = self.browser.find_element(*MainPageLocators.NEXT_P)
        next_p.click()
        time.sleep(2)
        first_p = self.browser.find_element(*MainPageLocators.FIRST_P)
        first_p.click()
        time.sleep(2)

    def new_comment(self):
        logo = self.browser.find_element(*MainPageLocators.LOGO)
        logo.click()
        pet_details = self.browser.find_element(*MainPageLocators.PET_DETAILS)
        pet_details.click()
        time.sleep(1)
        comment_field = self.browser.find_element(*MainPageLocators.COMMENT_FIELD)
        time.sleep(1)
        comment_field.send_keys("abcd")
        time.sleep(1)
        save_comment_btn = self.browser.find_element(*MainPageLocators.SAVE_COMMENT_BTN)
        save_comment_btn.click()
        time.sleep(1)

    def go_to_dropdown(self):
        drop_down = self.browser.find_element(*MainPageLocators.DROP_DOWN)
        time.sleep(2)
        drop_down.click()

    def dog_dropdown(self):
        drop_down = self.browser.find_element(*MainPageLocators.DROP_DOWN)
        time.sleep(2)
        drop_down.click()
        dd_dog = self.browser.find_element(*MainPageLocators.DD_DOG)
        time.sleep(2)
        dd_dog.click()
        time.sleep(2)

    def reptile_dropdown(self):
        drop_down = self.browser.find_element(*MainPageLocators.DROP_DOWN)
        time.sleep(2)
        drop_down.click()
        time.sleep(2)
        dd_reptile = self.browser.find_element(*MainPageLocators.DD_REPTILE)
        time.sleep(2)
        dd_reptile.click()
        time.sleep(2)

    def hamster_dropdown(self):
        drop_down = self.browser.find_element(*MainPageLocators.DROP_DOWN)
        time.sleep(2)
        drop_down.click()
        time.sleep(2)
        dd_hamster = self.browser.find_element(*MainPageLocators.DD_HAMSTER)
        time.sleep(2)
        dd_hamster.click()
        time.sleep(2)

    def go_to_amy(self):
        filter_field = self.browser.find_element(*MainPageLocators.FILTER_FIELD)
        filter_field.send_keys("Amy")
        header = self.browser.find_element(*MainPageLocators.HEADER)
        header.click()
        time.sleep(2)
        amy_btn = self.browser.find_element(*MainPageLocators.AMY_BTN)
        amy_btn.click()
        time.sleep(5)

    def go_to_dori(self):
        filter_field = self.browser.find_element(*MainPageLocators.FILTER_FIELD)
        filter_field.send_keys("Dori")
        header = self.browser.find_element(*MainPageLocators.HEADER)
        header.click()
        time.sleep(2)
        dori_btn = self.browser.find_element(*MainPageLocators.DORI_BTN)
        dori_btn.click()
        time.sleep(5)

    def open_pet_picture(self):
        logo = self.browser.find_element(*MainPageLocators.LOGO)
        logo.click()
        pet_details = self.browser.find_element(*MainPageLocators.PET_DETAILS)
        pet_details.click()
        pet_picture = self.browser.find_element(*MainPageLocators.PET_PICTURE)
        time.sleep(2)
        pet_picture.click()
        time.sleep(2)
        close_button = self.browser.find_element(*MainPageLocators.CLOSE_BUTTON)
        close_button.click()
        time.sleep(2)
