from .base_page import BasePage
from .locators import ProductPageLocators

class ProductPage(BasePage):
    def add_product_to_basket(self):
        basket = self.browser.find_element(*ProductPageLocators.BASKET_BUTTON)
        basket.click()
        BasePage.solve_quiz_and_get_code(self)

    def should_be_correct_product_name(self):
        name_in_title = self.browser.find_element(*ProductPageLocators.NAME_PRODUCT).text
        name_in_massange = self.browser.find_element(*ProductPageLocators.NAME_IN_MASSANGE).text
        BasePage.its_elements_equal(self, name_in_title, name_in_massange)
        

    def should_be_correct_price(self):
        price_in_title = self.browser.find_element(*ProductPageLocators.PRICE_PRODUCT).text
        price_in_massange = self.browser.find_element(*ProductPageLocators.PRICE_PRODUCT_IN_MASSANGE).text
        BasePage.its_elements_equal(self, price_in_title, price_in_massange)