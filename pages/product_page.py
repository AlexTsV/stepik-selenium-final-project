from .base_page import BasePage
from .locators import BasketPageLocators


class ProductPage(BasePage):
    def add_product_to_basket(self):
        add_product = self.browser.find_element(*BasketPageLocators.ADD_TO_BASKET_BUTTON)
        add_product.click()

    def should_be_add_to_basket_button(self):
        assert self.is_element_present(
            *BasketPageLocators.ADD_TO_BASKET_BUTTON), "Add to basket button is not presented"

    def should_be_product_added_message(self):
        assert self.is_element_present(*BasketPageLocators.PRODUCT_ADDED_MESSAGE)

    def should_be_product_price_message(self):
        assert self.is_element_present(*BasketPageLocators.PRODUCT_PRICE_MESSAGE)

    def catalog_price_must_be_equal_basket_price(self):
        product_price = self.browser.find_element(*BasketPageLocators.PRODUCT_PRICE).text
        basket_price = self.browser.find_element(*BasketPageLocators.PRODUCT_PRICE_MESSAGE).text
        assert product_price == basket_price.split(" ")[-1], "Catalog price and basket price is different"

    def product_catalog_name_must_math_product_basket_name(self):
        product_catalog_name = self.browser.find_element(*BasketPageLocators.PRODUCT_NAME).text
        product_name_in_product_added_message = self.browser.find_element(
            *BasketPageLocators.PRODUCT_NAME_IN_ADDED_TO_BASKET_MESSAGE).text
        print(product_name_in_product_added_message)
        assert product_catalog_name == product_name_in_product_added_message, \
            'Product in catalog and product in basket is different'
