from pages.base_page import BasePage
from pages.locators.constructor_locators import ConstructorPageLocators


class ConstructorPage(BasePage):
    def click_rub(self):
        assert self.is_element_present(*ConstructorPageLocators.BT_RUB), 'In BT_RUB is not presented'
        bt = self.browser.find_element(*ConstructorPageLocators.BT_RUB)
        bt.click()

    def click_dol(self):
        assert self.is_element_present(*ConstructorPageLocators.BT_DOL), 'In BT_DOL is not presented'
        bt = self.browser.find_element(*ConstructorPageLocators.BT_DOL)
        bt.click()

    def input_first_sum(self, text):
        assert self.is_element_present(*ConstructorPageLocators.IN_FS), 'In IN_FS is not presented'
        i = self.browser.find_element(*ConstructorPageLocators.IN_FS)
        i.click()
        i.send_keys(text)

    def input_fxus(self, text):
        assert self.is_element_present(*ConstructorPageLocators.IN_FXUS), 'In IN_FXUS is not presented'
        i = self.browser.find_element(*ConstructorPageLocators.IN_FXUS)
        i.click()
        i.send_keys(text)

    def input_fxde(self, text):
        assert self.is_element_present(*ConstructorPageLocators.IN_FXDE), 'In IN_FXDE is not presented'
        i = self.browser.find_element(*ConstructorPageLocators.IN_FXDE)
        i.click()
        i.send_keys(text)

    def input_fxcn(self, text):
        assert self.is_element_present(*ConstructorPageLocators.IN_FXCN), 'In IN_FXCN is not presented'
        i = self.browser.find_element(*ConstructorPageLocators.IN_FXCN)
        i.click()
        i.send_keys(text)

    def input_fxrl(self, text):
        assert self.is_element_present(*ConstructorPageLocators.IN_FXRL), 'In IN_FXRL is not presented'
        i = self.browser.find_element(*ConstructorPageLocators.IN_FXRL)
        i.click()
        i.send_keys(text)

    def should_be_portfolio(self):
        assert self.is_element_present(*ConstructorPageLocators.FD_PORT)
        assert self.is_element_present(*ConstructorPageLocators.FD_COMP)
        assert self.is_element_present(*ConstructorPageLocators.FD_HIST)
        assert self.is_element_present(*ConstructorPageLocators.FD_ANALYSE)
