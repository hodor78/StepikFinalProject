from selenium.webdriver.common.by import By

class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators:
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")

class ProductPageLocators:
    ADD_TO_BASKET = (By.CSS_SELECTOR, ".btn-add-to-basket")
    ORIGINAL_ITEM_NAME = (By.CSS_SELECTOR, "div.product_main h1")
    BASKET_ITEM_NAME = (By.CSS_SELECTOR, ".alert-success:nth-child(1) strong")
    ORIGINAL_ITEM_PRICE = (By.CSS_SELECTOR, ".product_main .price_color")
    BASKET_ITEM_PRICE = (By.CSS_SELECTOR, ".alertinner :nth-child(1) strong")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, ".alert-success:nth-child(1)")

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
