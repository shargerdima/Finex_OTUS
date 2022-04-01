from pages.base_page import BasePage
from pages.locators.robo_locators import RoboPageLocators


class RoboPage(BasePage):
    def robo(self):
        assert self.is_element_present(*RoboPageLocators.BT_ROBO), 'In BT_ROBO is not presented'
        bt = self.browser.find_element(*RoboPageLocators.BT_ROBO)
        bt.click()

    def click_rub(self):
        assert self.is_element_present(*RoboPageLocators.BT_RUB), 'In BT_RUB is not presented'
        bt = self.browser.find_element(*RoboPageLocators.BT_RUB)
        bt.click()

    def click_dol(self):
        assert self.is_element_present(*RoboPageLocators.BT_DOL), 'In BT_DOL is not presented'
        bt = self.browser.find_element(*RoboPageLocators.BT_DOL)
        bt.click()

    def input_first_sum(self, text):
        assert self.is_element_present(*RoboPageLocators.IN_FS), 'In IN_FS is not presented'
        i = self.browser.find_element(*RoboPageLocators.IN_FS)
        i.click()
        i.send_keys(text)

    def input_monthly_top_us(self, text):
        assert self.is_element_present(*RoboPageLocators.IN_MT), 'In IN_MT is not presented'
        i = self.browser.find_element(*RoboPageLocators.IN_MT)
        i.click()
        i.send_keys(text)

    def investment_term_oy(self):
        assert self.is_element_present(*RoboPageLocators.BT_IT_OY), 'In BT_IT_OY is not presented'
        bt = self.browser.find_element(*RoboPageLocators.BT_IT_OY)
        bt.click()

    def level_risk_c(self):
        assert self.is_element_present(*RoboPageLocators.BT_LR_C), 'In BT_LR_C is not presented'
        bt = self.browser.find_element(*RoboPageLocators.BT_LR_C)
        bt.click()

    def accept(self):
        assert self.is_element_present(*RoboPageLocators.BT_A), 'In BT_A is not presented'
        bt = self.browser.find_element(*RoboPageLocators.BT_A)
        bt.click()

    def goal_invest(self):
        assert self.is_element_present(*RoboPageLocators.GOAL), 'In GOAL is not presented'
