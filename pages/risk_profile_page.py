import time

from selenium.common.exceptions import NoSuchElementException

from pages.base_page import BasePage
from pages.locators.risk_profile_locators import RiskProfilePageLocators


class RiskProfilePage(BasePage):
    def risk_profile(self):
        assert self.is_element_present(*RiskProfilePageLocators.BT_RP), 'In BT_RP is not presented'
        bt = self.browser.find_element(*RiskProfilePageLocators.BT_RP)
        bt.click()

    def should_be_result(self):
        assert self.is_element_present(*RiskProfilePageLocators.FD_RT), 'In FD_RT is not presented'

    def accept(self):
        assert self.is_element_present(*RiskProfilePageLocators.BT_A), 'In BT_A is not presented'
        bt = self.browser.find_element(*RiskProfilePageLocators.BT_A)
        bt.click()

    def question(self, s):
        for i in range(s):
            try:
                assert self.is_element_present(*RiskProfilePageLocators.BT_AN_A), 'In BT_AN_A is not presented'
                bt = self.browser.find_element(*RiskProfilePageLocators.BT_AN_A)
                bt.click()
                time.sleep(2)
                print('Вопрос №: ', i+1)
            except NoSuchElementException as e:
                print('Retry in 1 sec...', e)
                break
