from selenium.webdriver.common.by import By


class RiskProfilePageLocators:
    BT_RP = (By.XPATH, "//*[@class='Sidebar_menuItemText__2907j' and text()='Тест на ']")
    FD_RT = (By.XPATH, "//*[text()='Результаты теста на']")
    FD_TB = (By.XPATH, "//*[text()='Тип Б']")
    FD_MP = (By.XPATH, "//*[text()='Выгоднее']")
    BT_A = (By.XPATH, "//*[text()='Принимаю']")
    BT_AN_A = (By.XPATH, "//*[@class='MuiButton-label']")