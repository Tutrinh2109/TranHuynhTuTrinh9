# -*- coding: utf-8 -*-
"""
Created on Fri Aug 30 17:05:31 2024

@author: TranHuynhTuTrinh
"""

#Nhập 1 chữ cái, nếu là chữ thường thì đổi thành chữ hoa, ngược lại đổi  thành chữ thường.

chu_cai = input("Nhập một chữ cái: ")
if chu_cai.islower():
    chu_cai = chu_cai.upper()
    print("Kết quả:", chu_cai)
elif chu_cai.isupper():
    chu_cai = chu_cai.lower()
    print("Kết quả:", chu_cai)
else:
    print("Chữ cái không hợp lệ.")
