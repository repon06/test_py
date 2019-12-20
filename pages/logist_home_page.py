#!/usr/bin/env python
# -*- coding: utf-8 -*-

import logging

from selenium.webdriver.common import keys
from selenium.webdriver.common.by import By
from pages.base_page import Base_Page
from utils import file_helper
from utils.Transporter import Transporter
from utils.file_helper import File


class logist_home_page(Base_Page):
    "базовый класс страницы умная логистика"
    page_name = "страница умная логистика"

    def start(self):
        print(f'перешли к {self.page_name}')
        # self.url = ""
        # self.open(self.url)

        self.my_login = '.framePressHeader #LogoutButton'
        self.news = "//div[@id='form1_Новости_Заголовок#title_div']"  # '#form1_Новости_Заголовок#title_div'
        self.button_logistic_xpath = "//div[@id='themesCell_theme_4' and span[span[text()='Логистика']]]"  # "//div[span[span[text()='Логистика']]]"
        self.buttons = '#themesCellLimiter div'
        self.home_title = '.openedHomeTitle'  # 'Начальная страница'

        # ЛОГИСТИКА
        # справочники
        self.sprav = "//div/span[text()='Справочники']"
        self.sprav_transporters_sub = "//div[div[span[text()='Справочники']]]/div[@class='funcCmd']/div[span[text()='Перевозчики']]"
        # logger object
        logging.basicConfig(filename="logist_start.log", level=logging.INFO)
        self.log_obj = logging.getLogger('logist')

        # перевозчики
        self.transporters_title = "//div[@data-title='Перевозчики']"

        # div#grid_form6_Список
        self.table = 'div[id$=_Список_div] div[style]>div.gridContent'  # 'div[id$=_Список_div] .gridContent div.gridRow'  # 'div[id$=_Список_div] .gridContent[style]' # 'div#form6_Список_div .gridContent'
        self.table_row = 'div[id$=_Список_div] .gridContent div.gridRow'  # строки
        self.table_transporter_name = "div[id$=_Список_div] .gridContent div.gridRow div.gridCell[colindex='1']"
        self.table_transporter_inn = "div[id$=_Список_div] .gridContent div.gridRow div.gridCell[colindex='2']"

        # доп инфа по перевозчику
        self.transporters_name = 'div[id$=_НаименованиеСокр]'  # '#form6_НаименованиеСокр' # //div/div[contains(@id,'_НаименованиеСокр') and table]
        self.inn = 'div[id$=_ПеревозчикИНН]'  # '#form6_ПеревозчикИНН'  # text
        self.addr = 'div[id$=_ПеревозчикЮридическийАдрес_div]'  # "//div[@id='form6_ПеревозчикЮридическийАдрес_div']"  # text
        self.phones = 'div[id$=_ПеревозчикТелефоны_div]'  # '#form6_ПеревозчикТелефоны_div'  # text
        self.contacts = 'div[id$=_КонтактныеЛица_div]'  # '#form6_КонтактныеЛица_div'  # панелька
        self.transporters = 'div[id$=_ВодителиПеревозчика_div]'  # '#form6_ВодителиПеревозчика_div'  # text

        self.wait_page_load(By.XPATH, self.news)
        print('дождались загрузки главного окна Логистики')

    def goto_logistica(self):
        print('переходим в логистику / перевозчики')
        heared_buttons = self.driver.find_elements_by_css_selector(self.buttons)
        if len(heared_buttons) > 0:
            print('увидели меню')
            self.driver.find_element(By.XPATH, self.button_logistic_xpath).click()
            self.wait_page_load(By.XPATH, self.sprav)
            self.driver.find_element(By.XPATH, self.sprav_transporters_sub).click()
            self.wait_page_load(By.XPATH, self.transporters_title)

            print('пришли к перевозчикам')
        else:
            print('не увидели меню')

    def get_list_transporters_count(self):
        print('получаем видимых перевозчиков')
        # table = self.driver.find_element(By.CSS_SELECTOR, self.table)
        rows = self.driver.find_elements(By.CSS_SELECTOR, self.table_row)
        return len(rows)

    def get_list__transporters(self):
        print('получаем видимых перевозчиков')
        # table = self.driver.find_element(By.CSS_SELECTOR, self.table)
        transporter_names_element = self.driver.find_elements(By.XPATH, self.table_transporter_name)
        return transporter_names_element

    def get_transporter_info(self):
        transporters_name = self.driver.find_element(By.CSS_SELECTOR, self.transporters_name).text
        inn = self.driver.find_element(By.CSS_SELECTOR, self.inn).text
        addr = self.driver.find_element(By.CSS_SELECTOR, self.addr).text
        phones = self.driver.find_element(By.CSS_SELECTOR, self.phones).text
        contacts = self.driver.find_element(By.CSS_SELECTOR, self.contacts).text
        transporters = self.driver.find_element(By.CSS_SELECTOR, self.transporters).text
        return Transporter(transporters_name, inn, addr, phones, contacts, transporters)

    def get_all_list_transporters(self, file_path):
        # print('переходим по всем перевозчикам')
        table = self.driver.find_element(By.CSS_SELECTOR, self.table)
        rows = self.driver.find_elements(By.CSS_SELECTOR, self.table_row)
        old_transporter_name = ''
        if len(rows) > 0:
            rows[0].click()
            transp = self.get_transporter_info()
            old_transporter_name = transp.name
            print(transp.name)

        File().write_to_file(file_path, f'Наименование\t\tАдрес\t\tИнн\t\tТелефон\t\tКонтакты\t\tПеревозчики')

        for i in range(5000):
            # print(f'бродим по массиву {i}')
            table.send_keys(keys.Keys.DOWN)
            # self.driver.find_element(By.CSS_SELECTOR, self.table)[0].send_keys(keys.Keys.DOWN)
            # table.find_elements(By.CSS_SELECTOR, self.table_row)[0].click()
            transp = self.get_transporter_info()
            print(transp.name)
            if old_transporter_name != transp.name:
                File().write_to_file(file_path,
                                     f'{transp.name}\t\t{transp.addr}\t\t{transp.inn}\t\t{transp.phones}\t\t{transp.contacts}\t\t{transp.transporters}')
