from pages.base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
    def should_be_message_basket_is_empty(self):
        empty_basket_text = self.browser.find_element(*BasketPageLocators.EMPTY_BASKET_MESSAGE).text
        assert 'Your basket is empty' in empty_basket_text, 'Basket not empty, but should be'

    def should_be_no_items_in_basket(self):
        return self.is_not_element_present(*BasketPageLocators.BASKET_ITEM)
