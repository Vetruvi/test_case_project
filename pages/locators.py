from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    EMAIL_INPUT_LOGIN = (By.NAME, "login-username")
    PASSWORD_INPUT_LOGIN = (By.NAME, "login-password")
    EMAIL_INPUT_REGISTRATION = (By.NAME, "registration-email")
    PASSWORD_INPUT_REGISTRATION = (By.NAME, "registration-password1")
    PASSWORD_REPEAT_INPUT_REGISTRATION = (By.NAME, "registration-password2")

    LOGIN_BUTTON = (By.NAME, "login_submit")
    REGISTRATION_BUTTON = (By.NAME, "registration_submit")

    LOGIN_FORM = (By.ID, "login_form")
    REGISTRATION_FORM = (By.ID, "register_form")