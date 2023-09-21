from .base_page import BasePage
from .locators import ProductPageLocators
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

class ProductPage(BasePage):
    def add_product_to_basket_with_alert_check(self):
        basket = self.browser.find_element(*ProductPageLocators.BASKET_BUTTON)
        basket.click()
        BasePage.solve_quiz_and_get_code(self)

    def add_product_to_basket(self):
        basket = self.browser.find_element(*ProductPageLocators.BASKET_BUTTON)
        basket.click()

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.NAME_IN_MASSANGE), \
            "Success message is presented, but should not be"
    
    def should_succes_massage_dissapeard(self):
        assert self.is_disappeared(*ProductPageLocators.NAME_IN_MASSANGE), \
            "Success message in not desappeared, but should be"

    def should_be_correct_product_name(self):
        WebDriverWait(self.browser, 4).until(EC.presence_of_element_located(ProductPageLocators.NAME_PRODUCT))
        name_in_title = self.browser.find_element(*ProductPageLocators.NAME_PRODUCT).text
        name_in_massange = self.browser.find_element(*ProductPageLocators.NAME_IN_MASSANGE).text
        BasePage.its_elements_equal(self, name_in_title, name_in_massange)
        
    def should_be_correct_price(self):
        WebDriverWait(self.browser, 4).until(EC.presence_of_element_located(ProductPageLocators.PRICE_PRODUCT))
        price_in_title = self.browser.find_element(*ProductPageLocators.PRICE_PRODUCT).text
        price_in_massange = self.browser.find_element(*ProductPageLocators.PRICE_PRODUCT_IN_MASSANGE).text
        BasePage.its_elements_equal(self, price_in_title, price_in_massange)