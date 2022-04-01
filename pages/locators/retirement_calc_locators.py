from selenium.webdriver.common.by import By


class RetirementCalcPageLocators:
    BT_RETIR = (By.XPATH, "//*[@class='Sidebar_menuItemText__2907j' and text()='Пенсионный калькулятор']")
    BT_RUB = (By.XPATH, "//*[@class='MuiButton-label' and text()='₽']")
    BT_DOL = (By.XPATH, "//*[@class='MuiButton-label' and text()='$']")
    FD_ACC = (By.XPATH, "//*[text()='Вы накопите']")
    FD_RES = (By.XPATH, "//*[text()='Оценка результата']")
    BT_COL = (By.XPATH, "//*[text()='Собрать пенсионный']")
    FD_GC = (By.XPATH, "//*[text()='График накоплений']")
