from pages.base_page import BasePage
from pages.locators.retirement_calc_locators import RetirementCalcPageLocators


class RetirementCalcPage(BasePage):
    def retirement(self):
        assert self.is_element_present(*RetirementCalcPageLocators.BT_RETIR), 'In BT_ROBO is not presented'
        bt = self.browser.find_element(*RetirementCalcPageLocators.BT_RETIR)
        bt.click()

    def click_rub(self):
        assert self.is_element_present(*RetirementCalcPageLocators.BT_RUB), 'In BT_RUB is not presented'
        bt = self.browser.find_element(*RetirementCalcPageLocators.BT_RUB)
        bt.click()

    def click_dol(self):
        assert self.is_element_present(*RetirementCalcPageLocators.BT_DOL), 'In BT_DOL is not presented'
        bt = self.browser.find_element(*RetirementCalcPageLocators.BT_DOL)
        bt.click()

    def should_be_result(self):
        assert self.is_element_present(*RetirementCalcPageLocators.FD_ACC), 'In FD_ACC is not presented'
        assert self.is_element_present(*RetirementCalcPageLocators.FD_RES), 'In FD_RES is not presented'
        assert self.is_element_present(*RetirementCalcPageLocators.BT_COL), 'In BT_COL is not presented'
        assert self.is_element_present(*RetirementCalcPageLocators.FD_GC), 'In FD_GC is not presented'
