from selenium.webdriver.common.by import By


class RoboPageLocators:
    BT_ROBO = (By.XPATH, "//*[text()='Робо']")
    BT_RUB = (By.XPATH, "//*[@class='MuiButton-label' and text()='₽']")
    BT_DOL = (By.XPATH, "//*[@class='MuiButton-label' and text()='$']")
    IN_FS = (By.XPATH, "//*[@class='MuiInputBase-input MuiOutlinedInput-input']")
    IN_MT = (By.XPATH, "//*[@aria-label='Ежемесячные пополнения']")
    BT_IT_OY = (By.XPATH, "//*[text()='1 год']")
    BT_LR_C = (By.XPATH, "//*[text()='Консервативный']")
    BT_A = (By.XPATH, "//*[text()='Принимаю']")
    GOAL = (By.XPATH, "//*[@class='jss82']")