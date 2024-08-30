# -*- coding: utf-8 -*-
"""
Created on Wed Aug 28 18:26:11 2024

@author: TranHuynhTuTrinh
"""

"""
Viết chương trình cho phép nhập vào giờ, phút và giây theo định dạng 
hh:mm:ss. Hãy đổi ra giây và in kết quả ra màn hình.
"""

thoi_gian = input("Nhập thời gian theo định dạng hh:mm:ss: ")
gio, phut, giay = map(int, thoi_gian.split(':'))
tong_giay = gio * 3600 + phut * 60 + giay
print(f"Tổng số giây của {thoi_gian} là: {tong_giay}")