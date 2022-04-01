from selenium.webdriver.common.by import By


class IisPageLocators:
    BT_IIS = (By.XPATH, "//*[@class='Sidebar_menuItemText__2907j' and text()='Калькулятор ИИС']")
    FD_TA = (By.XPATH, "//*[text()='Тип А']")
    FD_TB = (By.XPATH, "//*[text()='Тип Б']")
    FD_MP = (By.XPATH, "//*[text()='Выгоднее']")
