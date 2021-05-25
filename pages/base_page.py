from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from .locators import YandexPageLocators
from selenium.webdriver.common.keys import Keys
import time

class BasePage:

    def __init__(self, browser):  # конструктор, принимает browser — экземпляр webdriver
        self.browser = browser
        self.base_url = "https://yandex.ru/"

    def find_element(self, locator, time=10):  # ищет один элемент и возвращает его
        return WebDriverWait(self.browser, time).until(EC.presence_of_element_located(locator),
                                                    message=f"Can't find element by locator {locator}")

    def find_elements(self, locator, time=10):  # ищет элементы и возвращает список
        return WebDriverWait(self.browser, time).until(EC.presence_of_all_elements_located(locator),
                                                    message=f"Can't find elements by locator {locator}")

    def go_to_main(self):  # переходит на главную страницу яндекса
        return self.browser.get(self.base_url)

    def switch_to_new_tab(self):  # получает url последней открытой вкладки и переходит на нее
        handles = self.browser.window_handles
        size = len(handles)
        self.browser.switch_to.window(handles[size-1])
        return self.browser.current_url