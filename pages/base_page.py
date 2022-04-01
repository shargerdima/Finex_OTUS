from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import ElementNotInteractableException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time


class BasePage(object):
    def __init__(self, browser):
        self.browser = browser
        self.url = "https://finex-etf.ru/calc/"

    def open(self):
        self.browser.get(self.url)
        self.browser.maximize_window()

    def is_element_present(self, how, what):
        try:
            self.browser.find_element(how, what)
        except NoSuchElementException:
            return False
        return True

    def is_element_present_sec(self, how, what, timeout):
        try:
            for i in range(timeout):
                try:
                    self.browser.find_element(how, what)
                    break
                except NoSuchElementException as e:
                    print('Retry in 1 sec...')
                    time.sleep(1)
                except ElementNotInteractableException as e:
                    print('Retry in 1 sec...')
                    time.sleep(1)
            else:
                raise e
        except TimeoutException:
            return False
        return True

    def is_not_element_present(self, how, what):
        try:
            print('wait start...')
            WebDriverWait(self.browser, 10).until_not(EC.visibility_of_element_located((how, what)))
            print('wait finish...')
        except TimeoutException:
            print('Timeout')
            return False
        except NoSuchElementException:
            print('NoSuchElement')
            return False
        except Exception as e:
            print('Error visibility!:\n', e)
            return False
        print('Not timeout and not such')
        return True

