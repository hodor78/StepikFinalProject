from .pages.product_page import ProductPage
from .pages.basket_page import BasketPage
from .pages.login_page import LoginPage
import time
import pytest

class TestUserAddToBasketFromProductPage:
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        url = "http://selenium1py.pythonanywhere.com/en-gb/accounts/login/"
        email = str(time.time()) + "@fakemail.org"
        password = "13132GbbO"
        self.page = LoginPage(browser, url)
        self.page.open()
        self.page.register_new_user(email=email, password=password)
        self.page.should_be_authorized_user()

    def test_user_cant_see_success_message(self, browser):
        url = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
        self.page = ProductPage(browser, url)
        self.page.open()
        self.page.should_not_be_success_message()

    def test_user_can_add_product_to_basket(self, browser):
        url = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
        self.page = ProductPage(browser, url)
        self.page.open()
        self.page.add_to_basket()
        self.page.solve_quiz_and_get_code()

def test_guest_should_be_promo_url(browser):
    url = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
    page = ProductPage(browser, url)
    page.open()
    page.should_be_promo_url()

def test_guest_can_add_product_to_basket(browser):
    url = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
    page = ProductPage(browser, url)
    page.open()
    page.add_to_basket()
    page.solve_quiz_and_get_code()

def test_guest_confirmation_about_added_item_to_basket_same_name_as_original(browser):
    url = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
    page = ProductPage(browser, url)
    page.open()
    page.add_to_basket()
    page.solve_quiz_and_get_code()
    page.checking_the_name_of_the_added_item_in_basket()

def test_guest_confirmation_about_added_item_to_basket_same_price_as_original(browser):
    url = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
    page = ProductPage(browser, url)
    page.open()
    page.add_to_basket()
    page.solve_quiz_and_get_code()
    page.checking_the_price_of_the_added_item_in_basket()

@pytest.mark.parametrize('link', ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
                                  pytest.param("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7", marks=pytest.mark.xfail),
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"])

def test_guest_can_add_product_to_basket(browser, link):
    url = f"{link}"
    page = ProductPage(browser, url)
    page.open()
    page.add_to_basket()
    page.solve_quiz_and_get_code()
    page.checking_the_name_of_the_added_item_in_basket()
    page.checking_the_price_of_the_added_item_in_basket()


@pytest.mark.skip
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    url = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = ProductPage(browser, url)
    page.open()
    page.add_to_basket()
    page.solve_quiz_and_get_code()
    page.should_not_be_success_message()

def test_guest_cant_see_success_message(browser):
    url = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = ProductPage(browser, url)
    page.open()
    page.should_not_be_success_message()

@pytest.mark.skip
def test_message_disappeared_after_adding_product_to_basket(browser):
    url = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = ProductPage(browser, url)
    page.open()
    page.add_to_basket()
    page.solve_quiz_and_get_code()
    page.should_disappear_success_massege()

def test_guest_should_see_login_link_on_product_page(browser):
    url = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, url)
    page.open()
    page.should_be_login_link()

def test_guest_can_go_to_login_page_from_product_page(browser):
    url = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, url)
    page.open()
    page.go_to_login_page()

def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    url = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = ProductPage(browser, url)
    page.open()
    page.go_to_basket_from_any_page()
    basket_page = BasketPage(browser, browser.current_url)
    basket_page.should_not_be_any_items_in_the_basket()
    basket_page.should_be_empty_basket_message()


