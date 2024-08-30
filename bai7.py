# -*- coding: utf-8 -*-
"""
Created on Wed Aug 28 18:43:23 2024

@author: TranHuynhTuTrinh
"""

"""
Nhập vào bán kính của hình tròn, tính và in ra chu vi, diện tích của hình 
tròn đó.
"""

import math
ban_kinh = float(input("Nhập bán kính của hình tròn: "))
chu_vi = 2 * math.pi * ban_kinh
dien_tich = math.pi * (ban_kinh ** 2)
lam_tron_chu_vi = round(chu_vi,2)
lam_tron_dien_tich = round(dien_tich,2)
print(f"Chu vi của hình tròn là: {lam_tron_chu_vi}")
print(f"Diện tích của hình tròn là: {lam_tron_dien_tich}")