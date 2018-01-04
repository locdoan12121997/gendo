#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
from gendo import Gendo
import requests
import re
gendo = Gendo("xoxb-243402108406-A76uco7GUr1alochyQxGzKvQ")


path = os.path.dirname(os.path.abspath(__file__))
path_to_yaml = os.path.join(path, 'config.yaml')
gendo1 = Gendo.config_from_yaml(path_to_yaml)

keywords = [u'ăn trưa','an trua','tra sua', u'trà sữa',u'cơm trưa', 'com trua', u'cơm', 'com', u'gà', 'ga']
req = requests.get('https://www.deliverynow.vn/Offer/LoadMore?pageIndex=0&provinceId=217')
coupon_info = req.json()

@gendo.listen_for('cookies')
def cookies(user, message):
    return 'I *LOVE* COOOOOOOOKIES!!!!'

@gendo.cron('0 9 * * *')
def cookies(user, message):
    return 'morning everyonee'


@gendo.listen_for('morning')
def morning(user, message):
    # make sure message is "morning" and doesn't just contain it.
    if message.strip() == 'morning':
        return "mornin' @{user.username}"

@gendo.listen_for('Hey')
@gendo.listen_for('hey')
def morning(user, message):
    # make sure message is "morning" and doesn't just contain it.
    if message.strip() == 'hey':
        return "helu @{user.username}"

# @gendo.cron('* * * * *')
# def morning_greeting():
#     gendo.speak(u"Good morning mọi ngườiiiii", "#random")

@gendo.cron('30 14 * * *')
@gendo.listen_for('eat')
def cronjob():
    gendo.speak(u"Chào mọi người. Em là Coupon Bot. Nhà em có nhiều coupon.\n", "#testbot")
    gendo.speak(u"Coupon nè, hihihi:\n","#testbot")
    for i in range(0, 9):
        url = 'https://www.deliverynow.vn/Offer/LoadMore?pageIndex=' + str(i) + '&provinceId=217'
        req = requests.get(url)
        coupon_info = req.json()

        for data in coupon_info['data']:
            if (data['Restaurant']['FullAddress'][-6:] == u"Quận 4") or (
                        #data['Restaurant']['FullAddress'][-15:] == u"Quận Bình Thạnh") or (
                        data['Restaurant']['FullAddress'][-6:] == u"Quận 3") or (
                        data['Restaurant']['FullAddress'][-6:] == u"Quận 7") or (
                        data['Restaurant']['FullAddress'][-6:] == u"Quận 1"):

                discount = "Discount: " + data['Title'][4: 8] + "\n"
                res_name = "Restaurant: " + data['Restaurant']['ResName'] + "\n"
                code = "Code: " + data['PromoCode'] + "\n"
                address = "Address: " + data['Restaurant']['FullAddress'] + "\n"
                link = "Link: " + 'https://www.deliverynow.vn' + data['DetailUrl']

                gendo.speak(discount + res_name + code + address + link,"#testbot")

@gendo.listen_for('bot ')
def morning(user, message):
    # make sure message is "morning" and doesn't just contain it.
    if message.strip() == 'hey':
        return "helu @{user.username}"


if __name__ == '__main__':
    gendo.run()