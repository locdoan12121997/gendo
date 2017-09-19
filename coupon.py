#!/usr/bin/env python
# -*- coding: utf-8 -*-
import requests
from gendo import Gendo
import json
import os, sys

keywords = [u'ăn trưa','an trua','tra sua', u'trà sữa',u'cơm trưa', 'com trua', u'cơm', 'com', u'gà', 'ga']

for i in range(0,9):
    url = 'https://www.deliverynow.vn/Offer/LoadMore?pageIndex=' + str(i) + '&provinceId=217'
    req = requests.get(url)
    coupon_info = req.json()

    for data in coupon_info['data']:
         if (data['Restaurant']['FullAddress'][-6:] == u"Quận 2") or (
             data['Restaurant']['FullAddress'][-15:] == u"Quận Bình Thạnh"):
             print data['Title'][:8]
             print data['Restaurant']['ResName']
             print data['PromoCode']
             print data['Restaurant']['FullAddress']
