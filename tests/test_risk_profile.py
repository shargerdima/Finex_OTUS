from pages.risk_profile_page import RiskProfilePage
from pages.open_page import *


class TestRiskProfile:

    def test_risk_profile(self, browser):
        try:
            open_session(browser)
            rpp = RiskProfilePage(browser)
            rpp.risk_profile()
            rpp.accept()
            rpp.question(9)
            rpp.should_be_result()

        finally:
            browser.quit()
