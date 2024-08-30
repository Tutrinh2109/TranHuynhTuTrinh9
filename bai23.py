# -*- coding: utf-8 -*-
"""
Created on Thu Aug 15 23:26:18 2024

@author: TuTrinh
"""

#Giải và biện luận phương trình bậc hai: ax2 + bx + c = 0

import math 
a = float(input("Nhập a: "))
b = float(input("Nhập b: "))
c = float(input("Nhập c: "))        
if a!=0:
    delta = b**2- 4*a*c
    if delta<0:
        print("Phương trình vô nghiệm")
    elif delta==0:
        x = -b/2*a
        print("Phương trình có nghiệm kép x1 = x2 = ",x)
    else:
        x1 = (-b + math.sqrt(delta))/(2*a)
        x2 = (-b - math.sqrt(delta))/(2*a)
        print(f"Phương trình có 2 nghiệm phân biệt là x1 = {x1} và x2 = {x2}")
else:
    print("Không phải phương trình bậc 2")
    