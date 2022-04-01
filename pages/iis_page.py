from pages.base_page import BasePage
from pages.locators.iis_locators import IisPageLocators


class IisPage(BasePage):
    def iis(self):
        assert self.is_element_present(*IisPageLocators.BT_IIS), 'In BT_IIS is not presented'
        bt = self.browser.find_element(*IisPageLocators.BT_IIS)
        bt.click()

    def should_be_result(self):
        assert self.is_element_present(*IisPageLocators.FD_TA), 'In FD_TA is not presented'
        assert self.is_element_present(*IisPageLocators.FD_TB), 'In FD_TB is not presented'
        assert self.is_element_present(*IisPageLocators.FD_MP), 'In FD_MP is not presented'
