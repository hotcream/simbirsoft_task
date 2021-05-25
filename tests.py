import time
from selenium import webdriver
import pytest
from selenium.webdriver.common.keys import Keys
from pages.main_page import MainPage


def test_counting_messages(browser):
    '''Подсчет количества сообщений с заголовком "Simbirsoft Тестовое задание" '''
    page = MainPage(browser)  # создаем объект страницы
    page.go_to_main()  # зайти на главную яндекса
    page.log_in()  # логинимся
    page.go_to_post()  # открываем почту
    page.switch_to_new_tab()  # переходим на новую вкладку
    page.count_messages()  # считаем сообщения с заданным заголовком
    page.send_a_message()