from .base_page import BasePage
from .locators import ProductPageLocators
from .locators import BasePageLocators


class ProductPage(BasePage):
    def add_product_to_basket(self):
        add_product = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON)
        add_product.click()

    def should_be_add_to_basket_button(self):
        assert self.is_element_present(
            *ProductPageLocators.ADD_TO_BASKET_BUTTON), "Add to basket button is not presented"

    def should_be_product_added_message(self):
        assert self.is_element_present(*ProductPageLocators.PRODUCT_ADDED_MESSAGE)

    def should_be_product_price_message(self):
        assert self.is_element_present(*ProductPageLocators.PRODUCT_PRICE_MESSAGE)

    def catalog_price_must_be_equal_basket_price(self):
        product_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text
        basket_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE_MESSAGE).text
        assert product_price == basket_price.split(" ")[-1], "Catalog price and basket price is different"

    def product_catalog_name_must_match_product_basket_name(self):
        product_catalog_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text
        product_name_in_product_added_message = self.browser.find_element(
            *ProductPageLocators.PRODUCT_NAME_IN_ADDED_TO_BASKET_MESSAGE).text
        assert product_catalog_name == product_name_in_product_added_message, \
            'Product in catalog and product in basket is different'

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.PRODUCT_ADDED_MESSAGE), \
            "Success message is presented, but should not be"

    def success_message_should_disappear(self):
        assert self.is_disappeared(*ProductPageLocators.PRODUCT_ADDED_MESSAGE), "Success message does not disappeared"

    def go_to_login_page_from_product_page(self):
        login_link = self.browser.find_element(*BasePageLocators.LOGIN_LINK)
        login_link.click()
