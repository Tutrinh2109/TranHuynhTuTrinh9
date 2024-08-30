# -*- coding: utf-8 -*-
"""
Created on Fri Aug 30 20:57:11 2024

@author: TranHuynhTuTrinh
"""

#Cho số xe (gồm 4 chữ số) của bạn. Cho biết số xe của bạn được mấy nút?

a = int(input("Nhập số thứ nhất: "))
b = int(input("Nhập số thứ hai: "))
c = int(input("Nhập số thứ ba: "))
d = int(input("Nhập số thứ tư: "))
tong = a + b + c + d
so_nut = tong % 10
print(f"Số nút là: {so_nut}")
