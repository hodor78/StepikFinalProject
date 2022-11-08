from .base_page import BasePage
from .locators import ProductPageLocators



class ProductPage(BasePage):

    def add_to_basket(self):
        button = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET).click()

    def checking_the_name_of_the_added_item_in_basket(self):
        item_name_original = self.browser.find_element(*ProductPageLocators.ORIGINAL_ITEM_NAME).text
        item_name_basket = self.browser.find_element(*ProductPageLocators.BASKET_ITEM_NAME).text
        assert item_name_original == item_name_basket, "item name in the basket is not the same as original"

    def checking_the_price_of_the_added_item_in_basket(self):
        item_price_original = self.browser.find_element(*ProductPageLocators.ORIGINAL_ITEM_PRICE).text
        item_price_basket = self.browser.find_element(*ProductPageLocators.BASKET_ITEM_PRICE).text
        assert item_price_original == item_price_basket, "item price in the basket is not the same as original"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), "Success message is presented, but should not be"

    def should_disappear_success_massege(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), "Success message is presented, but should not be"

    def should_be_promo_url(self):
        assert "?promo=newYear" in self.browser.current_url, "'?promo=newYear' is not present in the url"





