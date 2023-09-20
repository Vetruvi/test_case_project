from .base_page import BasePage
from .locators import BasketPageLocators

class BasketPage(BasePage):

    def busket_should_be_empty(self):
        assert self.is_not_element_present(*BasketPageLocators.PRODUCTS_IN_BUSKET), "Busket not empty"

    def message_empty_busket_should_be(self):
        assert self.is_element_present(*BasketPageLocators.MESSAGE_EMPTY_BASKET), "There is no message"