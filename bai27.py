# -*- coding: utf-8 -*-
"""
Created on Fri Aug 30 20:07:16 2024

@author: TranHuynhTuTrinh
"""
"""
Viết chương trình tính diện tích và chu vi các hình: hình vuông (v), hình chữ
nhật (n) và hình tròn (t) với những thông tin được nhập từ bàn phím.
"""

import math
hinh = input("Nhập hình cần tính (v: vuông, n: chữ nhật, t: tròn): ")
if hinh == "v":
    canh = float(input("Nhập độ dài cạnh hình vuông: "))
    dien_tich = canh**2
    chu_vi = canh * 4
elif hinh == "n":
    chieu_dai = float(input("Nhập chiều dài hình chữ nhật: "))
    chieu_rong = float(input("Nhập chiều rộng hình chữ nhật: "))
    dien_tich = chieu_dai * chieu_rong
    chu_vi = (chieu_dai + chieu_rong) * 2
elif hinh == "t":
    ban_kinh = float(input("Nhập bán kính hình tròn: "))
    dien_tich = math.pi * ban_kinh**2
    chu_vi = 2 * math.pi * ban_kinh
else:
    print("Hình nhập không hợp lệ")
print(f"Diện tích là: {dien_tich} và chu vi là: {chu_vi}")
