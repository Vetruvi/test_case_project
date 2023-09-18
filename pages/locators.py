from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    EMAIL_INPUT_LOGIN = (By.NAME, 'login-username')
    PASSWORD_INPUT_LOGIN = (By.NAME, 'login-password')
    EMAIL_INPUT_REGISTRATION = (By.NAME, 'registration-email')
    PASSWORD_INPUT_REGISTRATION = (By.NAME, 'registration-password1')
    PASSWORD_REPEAT_INPUT_REGISTRATION = (By.NAME, 'registration-password2')

    LOGIN_BUTTON = (By.NAME, 'login_submit')
    REGISTRATION_BUTTON = (By.NAME, 'registration_submit')

    LOGIN_FORM = (By.ID, 'login_form')
    REGISTRATION_FORM = (By.ID, 'register_form')

class ProductPageLocators():
    BASKET_BUTTON = (By.CLASS_NAME, 'btn.btn-lg.btn-primary.btn-add-to-basket')

    NAME_PRODUCT = (By.XPATH, '//div[@class = "col-sm-6 product_main"]//h1')
    NAME_IN_MASSANGE = (By.XPATH, '//div[@class = "alertinner "][1]//strong')

    PRICE_PRODUCT = (By.XPATH, '//div[@class = "col-sm-6 product_main"]//p[@class = "price_color"]')
    PRICE_PRODUCT_IN_MASSANGE = (By.XPATH, '//div[@class = "alertinner "]//p//strong')