from pages.robo_page import RoboPage
from pages.open_page import *


class TestRobo:

    def test_robo_rub(self, browser):
        try:
            open_session(browser)
            cp = RoboPage(browser)
            cp.robo()
            cp.click_rub()
            cp.input_first_sum('0')
            cp.input_monthly_top_us('0')
            cp.investment_term_oy()
            cp.level_risk_c()
            cp.accept()
            cp.goal_invest()

        finally:
            browser.quit()

    def test_robo_dol(self, browser):
        try:
            open_session(browser)
            cp = RoboPage(browser)
            cp.robo()
            cp.click_dol()
            cp.input_first_sum('0')
            cp.input_monthly_top_us('0')
            cp.investment_term_oy()
            cp.level_risk_c()
            cp.accept()
            cp.goal_invest()

        finally:
            browser.quit()
