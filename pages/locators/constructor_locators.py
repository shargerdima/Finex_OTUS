from selenium.webdriver.common.by import By


class ConstructorPageLocators:
    BT_RUB = (By.XPATH, "//*[@class='MuiButton-label' and text()='₽']")
    BT_DOL = (By.XPATH, "//*[@class='MuiButton-label' and text()='$']")
    IN_FS = (By.XPATH, "//*[@class='MuiInputBase-input MuiOutlinedInput-input']")
    IN_FXUS = (By.XPATH, "//*[@data-testid='filterFundInput-FXUS']")
    IN_FXDE = (By.XPATH, "//*[@data-testid='filterFundInput-FXDE']")
    IN_FXCN = (By.XPATH, "//*[@data-testid='filterFundInput-FXCN']")
    IN_FXRL = (By.XPATH, "//*[@data-testid='filterFundInput-FXRL']")
    FD_PORT = (By.XPATH, "//*[text()='Ваш портфель']")
    FD_COMP = (By.XPATH, "//*[text()='Состав портфеля']")
    FD_HIST = (By.XPATH, "//*[text()='Историческая динамика']")
    FD_ANALYSE = (By.XPATH, "//*[text()='Анализ портфеля']")
