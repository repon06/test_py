#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests
from zeep import Client


class SoapClient(object):

    def get_track_info(self, track_code):
        print(track_code)

        client = Client('https://tracking.russianpost.ru/rtm34?wsdl')
        result = client.service.getOperationHistory()
        print(result)
