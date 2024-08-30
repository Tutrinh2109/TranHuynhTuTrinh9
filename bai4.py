# -*- coding: utf-8 -*-
"""
Created on Wed Aug 21 18:04:57 2024

@author: TranHuynhTuTrinh 
"""

"""
Viết chương trình cho phép nhập vào số nguyên dương N có 2 chữ số. Xuất 
ra màn hình tổng các chữ số của N.
"""

N = int (input("Nhập vào số nguyên dương có 2 chữ số: "))
if 10 <= N <= 99:
    hang_chuc = N // 10
    hang_don_vi = N % 10
    tong_N = hang_chuc + hang_don_vi
    print(f"Tổng các chữ số của {N} là: {hang_chuc} + {hang_don_vi} = {tong_N}")
else:
    print("Không phải số nguyên dương có 2 chữ số")
    