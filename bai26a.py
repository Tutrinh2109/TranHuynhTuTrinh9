# -*- coding: utf-8 -*-
"""
Created on Fri Aug 30 22:10:11 2024

@author: TranHuynhTuTrinh
"""
"""
(a) Cho ba số a, b, c được nhập vào từ bàn phím. Hãy in ra màn hình theo 
thứ tự tăng dần các số (Chỉ dùng 1 biến phụ).
"""

a = float(input("Nhập a: "))
b = float(input("Nhập b: "))
c = float(input("Nhập c: "))
if a > b:
    temp = a
    a = b
    b = temp
if a > c:
    temp = a
    a = c
    c = temp
if b > c:
    temp = b
    b = c
    c = temp
print("Thứ tự tăng dần là: ", a,b,c)