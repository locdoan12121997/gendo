#!/usr/bin/env python
# -*- coding: utf-8 -*-
import requests
from gendo import Gendo
import json
import os, sys

keywords = [u'ăn trưa','an trua','tra sua', u'trà sữa',u'cơm trưa', 'com trua', u'cơm', 'com', u'gà', 'ga']

req = requests.get('https://www.deliverynow.vn/Offer/LoadMore?pageIndex=0&provinceId=217')
coupon_info = req.json()


req = requests.get('https://www.deliverynow.vn/Offer/LoadMore?pageIndex=0&provinceId=217')
coupon_info = req.json()


input_dict = coupon_info
output_dict = [x:  for x in input_dict['data'] if (x['Restaurant']['FullAddress'][-6:]==u"Quận 3") or (x['Restaurant']['FullAddress'][-15:]==u"Quận Bình Thạnh")]
{k: v for k, v in input_dict['data'].iteritems() if (['Restaurant']['FullAddress'][-6:]==u"Quận 3") or (['Restaurant']['FullAddress'][-15:]==u"Quận Bình Thạnh")}
print type(input_dict)
print type(output_dict)

for data in output_dict['data']:
    print data['Title'][:8]
    print data['Restaurant']['ResName']
    print data['PromoCode']
