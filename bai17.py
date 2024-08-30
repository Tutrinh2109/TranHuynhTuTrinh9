# -*- coding: utf-8 -*-
"""
Created on Thu Aug 29 18:32:23 2024

@author: TranHuynhTuTrinh
"""
#Cho 3 số nguyên. Cho biết số lớn nhất và nhỏ nhất?

a = int(input("Nhập số nguyên thứ nhất: "))
b = int(input("Nhập số nguyên thứ hai: "))
c = int(input("Nhập số nguyên thứ ba: "))
so_lon_nhat = max(a,b,c)
so_nho_nhat = min(a,b,c)
print(f"Số lớn nhất là: {so_lon_nhat}")
print(f"Số nhỏ nhất là: {so_nho_nhat}")