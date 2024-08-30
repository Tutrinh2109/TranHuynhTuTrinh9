# -*- coding: utf-8 -*-
"""
Created on Thu Aug 29 18:12:01 2024

@author: TranHuynhTuTrinh
"""

#Nhập lần lượt ngày, tháng, năm sinh.

#a) Ngày/tháng/năm (Nhập 20 8 1990 thì xuất 20/8/1990)
ngay = int(input("Nhập ngày sinh: "))
thang = int(input("Nhập tháng sinh: "))
nam = int(input("Nhập năm sinh: "))
print(f"Ngày/tháng/năm: {ngay}/{thang}/{nam}")

#b) Ngày/tháng/năm (Nhập 20 8 1990 thì xuất 20/8/90)
nam_2_chu_so = str(nam)[-2:]
print(f"Ngày/tháng/năm: {ngay}/{thang}/{nam_2_chu_so}")

#c) Năm/tháng/ngày (Nhập 20 8 1990 thì xuất 1990/8/20)
print(f"Năm/tháng/ngày: {nam}/{thang}/{ngay}")
