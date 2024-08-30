# -*- coding: utf-8 -*-
"""
Created on Thu Aug 29 19:04:32 2024

@author: TranHuynhTuTrinh
"""

"""
Nhập 1 số bất kỳ. Hãy in giá trị (chuỗi) của số nguyên đó nếu nó có giá trị
từ 0 đến 9, ngược lại thông báo không đọc được.
"""

so = int(input("Nhập số bất kì: "))
x = {0:"Không", 1:"Một", 2:"Hai", 3:"Ba", 4:"Bốn", 5:"Năm", 6:"Sáu", 7:"Bảy", 8:"Tám",9:"Chín"}
if 0 <= so <= 9:
    print("Giá trị của số là:",(x[so]))
else:
    print("Không đọc được số")