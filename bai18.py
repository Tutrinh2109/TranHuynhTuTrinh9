# -*- coding: utf-8 -*-
"""
Created on Fri Aug 30 21:35:47 2024

@author: TranHuynhTuTrinh
"""
#Viết chương trình cho 2 giờ (giờ, phút, giây) và thực hiện cộng, trừ 2 giờ này.

def doi_thanh_giay(gio, phut, giay):
    return gio * 3600 + phut * 60 + giay

gio1 = int(input("Nhập giờ thứ nhất:"))
phut1 = int(input("Nhập phút thứ nhất:"))
giay1 = int(input("Nhập giây thứ nhất:"))

gio2 = int(input("Nhập giờ thứ hai:"))
phut2 = int(input("Nhập phút thứ hai:"))
giay2 = int(input("Nhập giây thứ hai:"))

tong_giay_1 = doi_thanh_giay(gio1, phut1, giay1)
tong_giay_2 = doi_thanh_giay(gio2, phut2, giay2)

tong_giay = tong_giay_1 + tong_giay_2
hieu_giay = tong_giay_1 - tong_giay_2

print(f"Tổng thời gian: {tong_giay} giây")
print(f"Hiệu thời gian: {hieu_giay} giây")

