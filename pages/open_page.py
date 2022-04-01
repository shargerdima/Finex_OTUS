from pages.base_page import BasePage


def open_session(browser):
    print('Open page')
    page = BasePage(browser)
    page.open()
