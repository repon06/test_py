#!/usr/bin/env python
# -*- coding: utf-8 -*-

class registry(object):

    def __init__(self, kd, fio, bd, rpo):
        self.kd = kd
        self.fio = fio
        self.bd = bd
        self.rpo = rpo
        fio_ = fio.split(' ')
        if len(fio_) == 3:
            self.lastname = fio_[0]
            self.firstname = fio_[1]
            self.middlename = fio_[2]
