from pages.base_page import BasePage
from .locators import BasketPageLocators
from selenium.common.exceptions import NoSuchElementException


class BasketPage(BasePage):
    def should_be_message_basket_is_empty(self):
        empty_basket_text = self.browser.find_element(*BasketPageLocators.EMPTY_BASKET_MESSAGE).text
        assert 'Your basket is empty' in empty_basket_text, 'Basket not empty, but should be'

    def should_be_no_items_in_basket(self):
        try:
            basket_item = self.browser.find_element(*BasketPageLocators.BASKET_ITEM)
        except NoSuchElementException:
            basket_item = False
        assert basket_item is False, 'Items in the basket, but should not'
