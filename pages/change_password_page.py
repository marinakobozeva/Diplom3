from pages.base_page import BasePage
from locators import Locators
from constants import Constants


class ChangePasswordPage(BasePage):

    def fill_email_form(self):
        self.set_text_to_element(Locators.INPUT_EMAIL, Constants.EMAIL)
        self.click_on_element(Locators.CHANGE_PASSWORD_BTN)

    def fill_password_form(self):
        self.set_text_to_element(Locators.NEW_PASSWORD_INPUT, Constants.PASSWORD)

    def is_password_visible(self):
        password_label = self.find_element_with_wait(Locators.NEW_PASSWORD_INPUT)
        return "text" in password_label.get_attribute('type')

    def is_password_invisible(self):
        password_label = self.find_element_with_wait(Locators.NEW_PASSWORD_INPUT)
        return "password" in password_label.get_attribute('type')







