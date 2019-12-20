#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests
import json


class RestClient(object):

    def get_post_info(self, track_code):
        from time import sleep

        # https://www.pochta.ru/new-tracking?utm_expid=.cn7RqAaMR7up8fY3Wk-Zdg.1&utm_referrer=https%3A%2F%2Fwww.pochta.ru%2F#63004930204681
        url_old = 'https://www.pochta.ru/new-tracking?p_p_id=trackingPortlet_WAR_portalportlet&p_p_lifecycle=2&p_p_state=normal&p_p_mode=view&p_p_resource_id=tracking.get-by-barcodes&p_p_cacheability=cacheLevelPage&p_p_col_id=column-1&p_p_col_count=1'
        url = 'https://www.pochta.ru/new-tracking'
        #headers = {'Content-Type': 'image/jpeg'}
        params = (
            ('p_p_id', 'trackingPortlet_WAR_portalportlet'),
            ('p_p_lifecycle', 2),
            ('p_p_state', 'normal'),
            ('p_p_mode', 'view'),
            ('p_p_resource_id', 'tracking.get-by-barcodes'),
            ('p_p_cacheability', 'cacheLevelPage'),
            ('p_p_col_id', 'column-1'),
            ('p_p_col_count', 1)
        )
        print(track_code)
        data = {'barcodes': 63004930204681}
        # response = requests.post(url, headers=headers, params=params, data=data)
        response = requests.post(url, params=params, data=json.dumps(data))
        print(response.status_code)
        print(response.content)

        print(response.url)
        print(url_old)
        print(response.url == url_old)
