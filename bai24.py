# -*- coding: utf-8 -*-
"""
Created on Fri Aug 30 16:42:35 2024

@author: TranHuynhTuTrinh
"""

#Nhập vào giờ, phút, giây. Kiểm tra xem giờ, phút, giây đó có hợp lệ hay không.

gio = int(input("Nhập giờ: "))
phut = int(input("Nhập phút: "))
giay = int(input("Nhập giây: "))
if 0 <= gio <= 24 and 0 <= phut <= 60 and 0 <= giay <= 60:
    print("Giờ, phút, giây hợp lệ")
else:
    print("Giờ, phút, giây không hợp lệ")
    