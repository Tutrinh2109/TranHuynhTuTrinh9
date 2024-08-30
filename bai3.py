# -*- coding: utf-8 -*-
"""
Created on Wed Aug 28 18:19:42 2024

@author: TranHuynhTuTrinh 
"""

"""
Viết chương trình nhập vào 2 số nguyên dương a, b, cho biết kết quả chia 
lấy phần nguyên và phần dư của a với b.
"""

a = int(input("Nhập số nguyên dương a: "))
b = int(input("Nhập số nguyên dương b: "))
if b == 0:
    print("Không thể chia cho 0.")
else:
    phan_nguyen = a // b
    phan_du = a % b
    print(f"Chia lấy phần nguyên của {a} cho {b} là: {phan_nguyen}")
    print(f"Chia lấy phần dư của {a} cho {b} là: {phan_du}")