from .pages.login_page import LoginPage

def test_should_be_login_url_present_for_guest(browser):
    url = "http://selenium1py.pythonanywhere.com/en-gb/accounts/login/"
    page = LoginPage(browser, url)
    page.open()
    page.should_be_login_url()

def test_should_be_login_form_present_for_guest(browser):
    url = "http://selenium1py.pythonanywhere.com/en-gb/accounts/login/"
    page = LoginPage(browser, url)
    page.open()
    page.should_be_login_form()

def test_should_be_register_form_present_for_guest(browser):
    url = "http://selenium1py.pythonanywhere.com/en-gb/accounts/login/"
    page = LoginPage(browser, url)
    page.open()
    page.should_be_register_form()