from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators():
    REGISTRATION_FORM = (By.CSS_SELECTOR, '#register_form')
    LOGIN_FORM = (By.CSS_SELECTOR, '#login_form')
    REGISTRATION_FORM_EMAIL = (By.CSS_SELECTOR, '#id_registration-email')
    REGISTRATION_FORM_PASSWORD = (By.CSS_SELECTOR, '#id_registration-password1')
    REGISTRATION_FORM_CONFORM_PASSWORD = (By.CSS_SELECTOR, '#id_registration-password2')
    REGISTRATION_BUTTON = (By.CSS_SELECTOR, '#register_form > button:nth-child(7)')


class ProductPageLocators():
    ADD_TO_BASKET_BUTTON = (By.CSS_SELECTOR, "#add_to_basket_form .btn")
    PRODUCT_ADDED_MESSAGE = (By.CSS_SELECTOR, "#messages > div:nth-child(1) > div")
    PRODUCT_PRICE_MESSAGE = (
        By.CSS_SELECTOR, "div.alert.alert-safe.alert-noicon.alert-info.fade.in > div > p:nth-child(1) > strong")
    PRODUCT_NAME = (By.CSS_SELECTOR, "#content_inner > article > div.row > div.col-sm-6.product_main > h1")
    PRODUCT_PRICE = (By.CSS_SELECTOR, "#content_inner > article > div.row > div.col-sm-6.product_main > p.price_color")
    PRODUCT_NAME_IN_ADDED_TO_BASKET_MESSAGE = (By.CSS_SELECTOR, "#messages > div:nth-child(1) > div > strong")


class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET_LINK = (By.CSS_SELECTOR, 'span.btn-group>a.btn.btn-default')
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")


class BasketPageLocators():
    EMPTY_BASKET_MESSAGE = (By.CSS_SELECTOR, "#content_inner > p:nth-child(1)")
    BASKET_ITEM = (By.CSS_SELECTOR, "div.basket-items:nth-child(7)")
