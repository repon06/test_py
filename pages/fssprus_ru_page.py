#!/usr/bin/env python
# -*- coding: utf-8 -*-

import logging
import time
import urllib  # 2.7 import urlparse
from urllib.parse import urlencode, quote_plus
from requests.utils import requote_uri
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from utils.config_helper import ConfigHelper


class fssprus_ru_page(object):
    "базовый класс страницы судебных приставов"
    page_name = "страница судебных приставов"

    def __init__(self, selenium_driver: WebDriver, base_url='https://fssprus.ru/'):
        # captcha modal

        self.captcha_modal = '.t-capcha'
        self.captcha_img = 'div#captcha-popup img#capchaVisual'
        self.input_code = 'input#captcha-popup-code'
        self.close = 'a.popup-but-close'
        self.submit_bt = 'intput.input-submit-capcha'
        self.loader = 'div.b-center-loader'

        # logger object
        logging.basicConfig(filename="mst_bank.log", level=logging.INFO)
        self.log_obj = logging.getLogger('mtsbank')

        self.base_url = base_url
        self.driver = selenium_driver
        self.driver.implicitly_wait(0)
        self.driver.maximize_window()
        self.start()

    def start(self):
        self.open()

    def open(self, url=""):
        url = self.base_url + url
        # if self.base_url not in self.driver.current_url:
        #    urlpars = urllib.parse.urlsplit(url)  # urlparse.urlparse(url)
        #    url = urlpars.scheme + "://%s:%s@" % (basic_auth_user, basic_auth_pass) + urlpars.netloc + urlpars.path
        self.driver.get(url)

    def find_fio_open_url(self, last_name, first_name, middle_name, birthday):
        # path = f'is[ip_preg]=&is[variant]=1&is[last_name]={last_name}&={first_name}&is[patronymic]={middle_name}&={birthday}'
        # url = self.base_url + 'iss/ip?' + path
        # print(url)

        # print(urllib.quote(url))
        # payload = {'username': 'administrator', 'password': 'xyz'}
        # path_encode = urlencode(path, quote_via=quote_plus)

        xxx = {'is[variant]': '1', 'is[last_name]': last_name, 'is[first_name]': first_name,
               'is[patronymic]': middle_name,
               'is[date]': birthday, 'is[region_id][0]': '-1'}
        print(f"birthday: {birthday}")
        url = self.base_url + 'iss/ip?' + urlencode(xxx)
        print(url)

        # print(requote_uri(path))
        # print(urllib.parse.quote(path))

        self.driver.get(url)

    def get_capcha_src(self):
        return self.driver.find_element_by_css_selector(self.captcha_img).get_attribute('src')

    def click_script(self, element: WebElement):
        """клик по hidden элементу"""
        self.driver.execute_script("arguments[0].click();", element)

    def script_edit_css_property(self, selector, prop_name, value):
        """изменить св-во элта скриптом"""
        js = "document.querySelector('{0}').style.{1}='{2}'".format(selector, prop_name, value)
        self.driver.execute_script(js)

    def write(self, msg, level='INFO'):
        self.log_obj.debug(msg, level)

    def wait(self, wait_seconds=5):
        time.sleep(wait_seconds)

    def wait_page_load(self, by, selector):
        """ожидаем загрузки страницы"""
        # try:
        wait = WebDriverWait(self.driver, 15)
        wait.until(EC.element_to_be_clickable((by, selector)))
        self.write('Страница %s загружена' % self.page_name)

    def submit(self):
        modal = self.driver.find_elements_by_css_selector(self.captcha_modal)
        if len(modal) > 0:
            button = modal[0].find_element(By.CSS_SELECTOR, self.submit_bt).click()

    def get_message(self):
        # text = elements[0].find_element(By.CSS_SELECTOR, self.notification_message).text
        # self.write("no found error msg")
        return None

    def close_modal(self):
        """если есть модалка - закрываем ее"""
        modal = self.driver.find_elements_by_css_selector(self.captcha_modal)
        if len(modal) > 0:
            modal[0].find_element(By.CSS_SELECTOR, self.close).click()

    def select_of_webelement(self, by, select, sub_select, value):
        element = self.driver.find_element(by, select)  # div.field
        element.click()

        sub_elements = self.driver.find_elements(by, sub_select)
        if len(sub_elements) > 0:
            for item in sub_elements:
                # print(item.text)
                if value in item.text:
                    item.click()
                    # ждем исчезновения
                    wait = WebDriverWait(self.driver, 15)
                    wait.until(EC.invisibility_of_element_located((By.CSS_SELECTOR, sub_select)))
                    return

    def captcha_click(self):
        self.driver.find_element(By.CSS_SELECTOR, self.captcha_img).click()

    def search_table(self):
        elements = self.driver.find_elements(By.CSS_SELECTOR, ".results-frame tbody>tr>td.first")
        print(len(elements))  # ([0].text)
