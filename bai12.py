# -*- coding: utf-8 -*-
"""
Created on Wed Aug 28 19:49:53 2024

@author: TranHuynhTuTrinh 
"""
#Xuất ra một số (nguyên, thực) ngẫu nhiên theo yêu cầu

import random
#Số nguyên ngẫu nhiên:
a = random.randrange(0,101,1)
print(f"Số nguyên ngẫu nhiên từ 0 đến 100 là: {a}")
b = random.randrange(50,100,1)
print(f"Số nguyên ngẫu nhiên từ 50 đến 99 là: {b}")
c = random.randrange(-39,80,1)
print(f"Số nguyên ngẫu nhiên từ -39 đến 79 là: {c}")
d = random.randrange(-79,-40,1)
print(f"Số nguyên ngẫu nhiên từ -79 đến -39 là: {d}")
#Số thực ngẫu nhiên:
e = random.uniform(0,100)
print(f"Số  ngẫu nhiên từ 0 đến 100 là: {e}")
f = random.uniform(50,99)
print(f"Số  ngẫu nhiên từ 50 đến 99 là: {f}")
g = random.uniform(-39,-79)
print(f"Số  ngẫu nhiên từ -39 đến 79 là: {g}")
h = random.uniform(-79,-39)
print(f"Số  ngẫu nhiên từ -79 đến -39 là: {h}")
