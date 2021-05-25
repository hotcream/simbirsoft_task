from .base_page import BasePage
from selenium.webdriver.common.keys import Keys
from .locators import YandexPageLocators
from .locators import MailPageLocators
import time


class MainPage(BasePage):

    def log_in(self, mail="simbirsofttask@yandex.ru", passw="010203qweR"):  # Авторизация
        enter_btn = self.find_element(YandexPageLocators.LOCATOR_ENTER_BUTTON)
        enter_btn.click()
        username_field = self.find_element(YandexPageLocators.LOCATOR_USERNAME_INPUT)
        username_field.send_keys(mail)
        submit_btn = self.find_element(YandexPageLocators.LOCATOR_SUBMIT_BUTTON)
        submit_btn.click()
        pass_field = self.find_element(YandexPageLocators.LOCATOR_PASSWORD_INPUT)
        pass_field.send_keys(passw)
        submit_btn = self.find_element(YandexPageLocators.LOCATOR_SUBMIT_BUTTON)
        submit_btn.click()

    def go_to_post(self):  # Открытие почты
        mail_button = self.find_element(YandexPageLocators.LOCATOR_MAIL_BUTTON)
        mail_button.click()

    def count_messages(self):  # считает сообщения с заданным заголовком
        self.number_of_messages = 0
        messages_title = self.find_elements(MailPageLocators.LOCATOR_MESSAGES_TITLE)
        for title in messages_title:
            if title.text == 'Simbirsoft Тестовое задание':
                self.number_of_messages += 1

    def send_a_message(self):  # отправляет сообщение
        send_a_message_button = self.find_element(MailPageLocators.LOCATOR_SEND_A_MESSAGE_BUTTON)
        send_a_message_button.click()
        time.sleep(2)
        to_whom_field_input = self.find_element(MailPageLocators.LOCATOR_TO_WHOM_INPUT)
        to_whom_field_input.send_keys('simbirsofttask@yandex.ru')
        title_field_input = self.find_element(MailPageLocators.LOCATOR_TITLE_INPUT)
        title_field_input.send_keys('Simbirsoft Тестовое задание. Рожков')
        message_text = self.find_element(MailPageLocators.LOCATOR_MESSAGE_INPUT_FIELD)
        message_text.send_keys(self.number_of_messages)
        send_button = self.find_element(MailPageLocators.LOCATOR_SEND_BUTTON)
        send_button.click()