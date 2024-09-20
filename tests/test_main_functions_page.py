from locators import Locators
from pages.main_functions_page import MainFunctionsPage
from constants import Constants
import allure

class TestMainFunctionsPage:
    @allure.title("переход по клику на «Конструктор»")
    def test_go_to_constructor_section(self, driver):
        main_functions_page = MainFunctionsPage(driver)
        main_functions_page.click_on_element(Locators.PERSONAL_ACCOUNT_BTN)
        main_functions_page.find_element_with_wait(Locators.SIGN_IN_TITLE)
        main_functions_page.click_on_element(Locators.CONSTRUCTOR_BTN)
        result = main_functions_page.find_element_with_wait(Locators.CONSTRUCTOR_TITLE)
        assert result

    @allure.title("переход по клику на «Лента заказов»")
    def test_go_to_order_list_section(self, driver):
        main_functions_page = MainFunctionsPage(driver)
        main_functions_page.click_on_element(Locators.PERSONAL_ACCOUNT_BTN)
        main_functions_page.find_element_with_wait(Locators.SIGN_IN_TITLE)
        main_functions_page.click_on_element(Locators.ORDERS_LIST_BTN)
        result = main_functions_page.find_element_with_wait(Locators.ORDER_LIST_TITLE)
        assert result


    @allure.title("если кликнуть на ингредиент, появится всплывающее окно с деталями")
    def test_poppup_with_ingredients_details(self, driver):
        main_functions_page = MainFunctionsPage(driver)
        main_functions_page.click_on_element(Locators.BURGER_LOCATOR)
        result = main_functions_page.find_element_with_wait(Locators.INGREDIENT_DETAILS_TITLE)
        assert result

    @allure.title("всплывающее окно закрывается кликом по крестику")
    def test_popup_close(self, driver):
        main_functions_page = MainFunctionsPage(driver)
        main_functions_page.click_on_element(Locators.BURGER_LOCATOR)
        popup = main_functions_page.wait_for_element_visible(Locators.INGREDIENT_POPUP)
        assert popup.is_displayed()
        main_functions_page.find_element_with_wait(Locators.INGREDIENT_DETAILS_TITLE)
        main_functions_page.click_on_element(Locators.CLOSE_ICON_BTN)
        popup = main_functions_page.wait_for_element_invisible(Locators.INGREDIENT_POPUP)
        assert not popup.is_displayed()

    @allure.title("при добавлении ингредиента в заказ, увеличивается каунтер данного ингредиента")
    def test_counter(self, driver):
        main_functions_page = MainFunctionsPage(driver)
        main_functions_page.drag_and_drop_item(Locators.SAUSE_SPICY_X_INGREDIENT, Locators.BASKET_LOCATOR)
        main_functions_page.find_element_with_wait(Locators.SAUSE_SPICY_X_INGREDIENT)
        counter = main_functions_page.get_text_from_element(Locators.SAUSE_SPICY_X_INGREDIENT_COUNTER)
        assert counter == "1"

    @allure.title("залогиненный пользователь может оформить заказ")
    def test_make_order_authorised_user(self, driver):
        main_functions_page = MainFunctionsPage(driver)
        main_functions_page.click_on_element(Locators.PERSONAL_ACCOUNT_BTN)
        main_functions_page.wait_for_page(Constants.PERSONAL_ACCOUNT_URL)
        main_functions_page.fill_login_form(Locators.INPUT_EMAIL, Constants.EMAIL, Locators.INPUT_PASSWORD, Constants.PASSWORD, Locators.SIGN_IN_BTN)
        main_functions_page.find_element_with_wait(Locators.CONSTRUCTOR_TITLE)
        main_functions_page.drag_and_drop_item(Locators.BUN, Locators.BASKET_LOCATOR)
        main_functions_page.drag_and_drop_item(Locators.SAUSE_SPICY_X_INGREDIENT, Locators.BASKET_LOCATOR)
        main_functions_page.click_on_element(Locators.MAKE_ORDER_BTN)
        result = main_functions_page.find_element_with_wait(Locators.ORDER_SUBTITLE)
        assert result






















