# -*- coding: utf-8 -*-
"""
Created on Thu Aug 29 18:44:26 2024

@author: TranHuynhTuTrinh
"""

#Nhập vào 4 số nguyên a, b, c, d. In ra màn hình số có giá trị nhỏ nhất.

a = int(input("Nhập số nguyên thứ nhất: "))
b = int(input("Nhập số nguyên thứ hai: "))
c = int(input("Nhập số nguyên thứ ba: "))
d = int(input("Nhập số nguyên thứ tư: "))
so_nho_nhat = a
if b < so_nho_nhat:
    so_nho_nhat = b
if c < so_nho_nhat:
    so_nho_nhat = c
if d < so_nho_nhat:
    so_nho_nhat = d
print(f"Số có giá trị nhỏ nhất là: {so_nho_nhat}")
