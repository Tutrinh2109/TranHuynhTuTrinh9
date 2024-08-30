# -*- coding: utf-8 -*-
"""
Created on Thu Aug 29 18:56:25 2024

@author: TranHuynhTuTrinh
"""

#Nhập vào 3 số a, b, c từ bàn phím. In ra màn hình số có giá trị lớn nhất

a = float(input("Nhập số thứ nhất: "))
b = float(input("Nhập số thứ hai: "))
c = float(input("Nhập số thứ ba: "))
so_lon_nhat = a
if b > so_lon_nhat:
    so_lon_nhat = b
if c > so_lon_nhat:
    so_lon_nhat = c
print(f"Số có giá trị lớn nhât là: {so_lon_nhat}")
