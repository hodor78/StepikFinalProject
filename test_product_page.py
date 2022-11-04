from .pages.product_page import ProductPage
import time
import pytest

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