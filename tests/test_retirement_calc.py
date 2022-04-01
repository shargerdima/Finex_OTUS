from pages.retirement_calc_page import RetirementCalcPage
from pages.open_page import *


class TestRetirementCalc:

    def test_retirement_rub(self, browser):
        try:
            open_session(browser)
            rcp = RetirementCalcPage(browser)
            rcp.retirement()
            rcp.click_rub()
            rcp.should_be_result()

        finally:
            browser.quit()

    def test_retirement_dol(self, browser):
        try:
            open_session(browser)
            rcp = RetirementCalcPage(browser)
            rcp.retirement()
            rcp.click_dol()
            rcp.should_be_result()

        finally:
            browser.quit()