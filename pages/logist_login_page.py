#!/usr/bin/env python
# -*- coding: utf-8 -*-

from selenium.webdriver.common.by import By
from pages.base_page import Base_Page


class logist_login_page(Base_Page):
    "базовый класс страницы авторизации в логистике"
    page_name = "страница авторизации в логистике"

    def start(self):
        print(f'перешли к {self.page_name}')
        self.url = ""
        self.open(self.url)

        # selector_of_elements
        self.auth_window = '.authWindow'
        self.user_name = 'input#userName'
        self.password = 'input#userPassword'
        self.ok = '#okButton'
        self.cansel = '#cancelButton'

        # ждем загрузки стр
        self.wait_page_load(By.CSS_SELECTOR, self.auth_window)
        print('дождались загрузки окна авторизации')

    def login(self, login, passw):
        auth_win = self.driver.find_elements_by_css_selector(self.auth_window)
        if len(auth_win) > 0:
            print('увидели окно авторизации')
            self.driver.find_element_by_css_selector(self.user_name).send_keys(login)
            self.driver.find_element_by_css_selector(self.password).send_keys(passw)
            self.driver.find_element_by_css_selector(self.ok).click()
            print('заполнили поля и нажали ОК')
            from pages.logist_home_page import logist_home_page
            return logist_home_page(selenium_driver=self.driver)
        else:
            print('не увидели окно авторизации')

    def get_capcha_src(self):
        return self.driver.find_element_by_css_selector('').get_attribute('src')
