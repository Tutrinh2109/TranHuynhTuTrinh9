# -*- coding: utf-8 -*-
"""
Created on Fri Aug 30 22:03:36 2024

@author: TranHuynhTuTrinh
"""
#(b) Nhập vào 1 số nguyên N sau đó in ra số có các con số theo thứ tự tăng dần.


# Nhập vào số nguyên N
N = input("Nhập một số nguyên N: ")
# Chuyển số thành chuỗi và sắp xếp các chữ số theo thứ tự tăng dần
sap_xep_so = sorted(N)
# Kết hợp các chữ số đã sắp xếp thành một chuỗi
chuoi_so = ''.join(sap_xep_so)
print("Số có các chữ số theo thứ tự tăng dần là:", chuoi_so)

