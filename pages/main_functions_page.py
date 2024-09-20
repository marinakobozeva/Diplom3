from pages.base_page import BasePage
from locators import Locators
from constants import Constants


class MainFunctionsPage(BasePage):

    def is_popup_visible(self):
        popup = self.find_element_with_wait(Locators.INGREDIENT_POPUP)
        return "visible" in popup.get_attribute('visibility')



