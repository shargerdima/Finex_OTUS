from pages.iis_page import IisPage
from pages.open_page import *


class TestIis:

    def test_iis_rub(self, browser):
        try:
            open_session(browser)
            ip = IisPage(browser)
            ip.iis()
            ip.should_be_result()

        finally:
            browser.quit()
