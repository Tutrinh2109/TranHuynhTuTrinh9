# -*- coding: utf-8 -*-
"""
Created on Thu Aug 29 15:15:15 2024

@author: TranHuynhTuTrinh
"""

import math
a = float(input("Nhập a: "))
b = float(input("Nhập b: "))
A = (((a+b)/(math.pow(a,1/3)+math.pow(b,1/3))) - math.pow(a*b,1/3)) / ((math.pow(a,1/3))-(math.pow(b,1/3)))**2
print("Kết quả là: ",A)

