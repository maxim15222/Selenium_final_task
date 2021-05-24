from selenium.webdriver.common.by import By


class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")
    REGISTER_EMAIL = (By.CSS_SELECTOR, "#id_registration-email")
    REGISTER_PASSWORD = (By.CSS_SELECTOR, "#id_registration-password1")
    REGISTER_PASSWORD_CONFIRM = (By.CSS_SELECTOR, "#id_registration-password2")
    REGISTER_BUTTON = (By.CSS_SELECTOR, "#register_form > button")

class ProductPageLocators():
    BUTTON_ADD_TO_BASKET = (By.CSS_SELECTOR, ".btn-add-to-basket")
    PRODUCT_NAME = (By.CSS_SELECTOR, '#content_inner .product_main h1')
    PRODUCT_PRICE = (By.CSS_SELECTOR, '#content_inner .product_main p')
    ADDED_PRODUCT_NAME = (By.CSS_SELECTOR, '#messages > .alert:nth-child(1) > .alertinner > strong ')
    BASKET_PRICE = (By.CSS_SELECTOR, '#messages > .alert:nth-child(3) > .alertinner > p > strong ')
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, '#messages > .alert:nth-child(1)')


class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET_LINK = (By.CSS_SELECTOR, ".header  .btn")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")


class BasketPageLocators():
    BASKET_ITEMS = (By.CSS_SELECTOR, ".basket-items")
    BASKET_TEXT = (By.CSS_SELECTOR, "#content_inner p")
