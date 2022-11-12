from .base_page import BasePage
from .locators import BasePageLocators

class BasketPage(BasePage):
    def should_not_be_any_items_in_the_basket(self):
        assert self.is_not_element_present(*BasePageLocators.BASKET_ITEMS), "You're not supposed to have any items in the basket at this stage"

    def should_be_empty_basket_message(self):
        assert self.is_element_present(*BasePageLocators.EMPTY_BASKET_MESSAGE), "There is no empty basket message"