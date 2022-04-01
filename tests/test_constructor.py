from pages.constructor_page import ConstructorPage
from pages.open_page import *


class TestConstructor:

    def test_constructor_rub(self, browser):
        try:
            open_session(browser)
            cp = ConstructorPage(browser)
            cp.click_rub()
            cp.input_first_sum('0')
            cp.input_fxus('30')
            cp.input_fxde('30')
            cp.input_fxcn('20')
            cp.input_fxrl('20')
            cp.should_be_portfolio()

        finally:
            browser.quit()

    def test_constructor_dol(self, browser):
        try:
            open_session(browser)
            cp = ConstructorPage(browser)
            cp.click_dol()
            cp.input_first_sum('0')
            cp.input_fxus('30')
            cp.input_fxde('30')
            cp.input_fxcn('20')
            cp.input_fxrl('20')
            cp.should_be_portfolio()

        finally:
            browser.quit()

