#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
from gendo import Gendo
import requests
gendo = Gendo("xoxb-243402108406-LIzxxrpI5ftpgQTUJSmX12I0")


path = os.path.dirname(os.path.abspath(__file__))
path_to_yaml = os.path.join(path, 'config.yaml')
gendo1 = Gendo.config_from_yaml(path_to_yaml)

keywords = [u'ăn trưa','an trua','tra sua', u'trà sữa',u'cơm trưa', 'com trua', u'cơm', 'com', u'gà', 'ga']
req = requests.get('https://www.deliverynow.vn/Offer/LoadMore?pageIndex=0&provinceId=217')
coupon_info = req.json()

@gendo.listen_for('cookies')
def cookies(user, message):
    return 'I *LOVE* COOOOOOOOKIES!!!!'


@gendo.listen_for('morning')
def morning(user, message):
    # make sure message is "morning" and doesn't just contain it.
    if message.strip() == 'morning':
        return "mornin' @{user.username}"

@gendo.listen_for('hey')
def morning(user, message):
    # make sure message is "morning" and doesn't just contain it.
    if message.strip() == 'hey':
        return "helu @{user.username}"

@gendo.cron('39 12 * * *')
def morning_greeting():
    gendo.speak(u"Chào mọi người", "#random")

@gendo.listen_for('test')
# @gendo.cron('*/1 * * * *')
def cronjob():
    gendo.speak("Heyy, new discount yooo:\n","#random")
    for i in range(0, 9):
        url = 'https://www.deliverynow.vn/Offer/LoadMore?pageIndex=' + str(i) + '&provinceId=217'
        req = requests.get(url)
        coupon_info = req.json()

        for data in coupon_info['data']:
            if (data['Restaurant']['FullAddress'][-6:] == u"Quận 2") or (
                        data['Restaurant']['FullAddress'][-15:] == u"Quận Bình Thạnh"):

                discount = "Discount: " + data['Title'][4: 8] + "\n"
                res_name = "Restaurant: " + data['Restaurant']['ResName'] + "\n"
                code = "Code: " + data['PromoCode'] + "\n"
                address = "Address: " + data['Restaurant']['FullAddress'] + "\n"
                link = "Link: " + 'https://www.deliverynow.vn' + data['DetailUrl']

                gendo.speak( discount  + res_name + code + address + link,"#random")

@gendo.listen_for('bot ')
def morning(user, message):
    # make sure message is "morning" and doesn't just contain it.
    if message.strip() == 'hey':
        return "helu @{user.username}"


# if __name__ == '__main__':
gendo.run()