#!/usr/bin/env python
# -*- coding: utf-8 -*-
import argparse
import random
import sys

from pages.fssprus_ru_page import fssprus_ru_page
from pages.logist_login_page import logist_login_page
from utils import img_helper
from utils.datetime_helper import get_date
from utils.driver_factory import DriverFactory
from utils.excel_helper import Excel
from utils.file_helper import File
from utils.img_helper import save_img_from_src, change_img


def createParser():
    parser = argparse.ArgumentParser()
    parser.add_argument('-p', '--path', default='D:\work\openDev\MTS\Проект реестра.xlsx')
    return parser


if __name__ == '__main__':
    parser = createParser()
    namespace = parser.parse_args(sys.argv[1:])
    print(namespace.path)

    registry_bank = Excel().read_file(namespace.path)
    # reg = registry(fio='бысьолв жегтс юичавмсч', bd='26.05.1984', kd='ПННСЗФ4515/810/13', rpo='80086633064356')

    item = 1
    print(registry_bank[item].fio)
    print(registry_bank[item].lastname)
    print(registry_bank[item].bd)
    print(get_date(registry_bank[item].bd))
    # print(registry_bank[6].fio.split(' '))

    #    for i in range(20):
    #        File().write_to_file('./logist.txt', '123')

    driver = DriverFactory().get_web_driver("chrome")

    logist_login = logist_login_page(selenium_driver=driver)
    logist_home = logist_login.login('ebistrova@utsl.ru', '01499')
    logist_home.goto_logistica()
    transporter_count = logist_home.get_list_transporters_count()
    transporter = logist_home.get_transporter_info()
    print(f'видим перевозчиков {transporter_count}')
    print(f'Перевозчик: {transporter.name}; {transporter.phones} ; {transporter.contacts}; {transporter.transporters}')
    logist_home.get_all_list_transporters()
    logist_home.wait(6000)

    driver.close()

    # login = ConfigHelper().getConfigOption('username1_valid', 'login')
    # password = ConfigHelper().getConfigOption("username1_valid", "password")
    fss_page = fssprus_ru_page(selenium_driver=driver)
    fss_page.find_fio_open_url(registry_bank[item].lastname, registry_bank[item].firstname,
                               registry_bank[item].middlename, get_date(registry_bank[item].bd))

    fss_page.wait(5)
    fss_page.search_table()

    jpeg_txt = fss_page.get_capcha_src()
    filepath = f"C:/temp/image{random.randint(0, 1000)}.jpeg"
    img_helper.save_img_from_src(jpeg_txt, filepath)
    img_helper.change_img(jpeg_txt, filepath)

    for i in range(100):
        fss_page.captcha_click()
        fss_page.wait(3)
        filepath = f"C:/temp/image{random.randint(0, 1000)}.jpeg"
        save_img_from_src(fss_page.get_capcha_src(), filepath)
        change_img(jpeg_txt, filepath)

    fss_page.close_modal()

    # def teardown():
    #    driver.close()
    #    request.addfinalizer(teardown)
    # return payment_page

    # yield driver
    driver.close()

#    rest = RestClient().get_post_info("63004930204681")
#    soap = SoapClient().get_track_info("63004930204681")
