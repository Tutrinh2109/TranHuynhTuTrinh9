# -*- coding: utf-8 -*-
"""
Created on Wed Aug 28 18:54:29 2024

@author: TranHuynhTuTrinh
"""

#Viết chương trình tính số đo kiểm tra sức khỏe BMI.

can_nang = float(input("Nhập cân nặng (kg): "))
chieu_cao = float(input("Nhập chiều cao (m): "))
BMI = can_nang / (chieu_cao**2)
lam_tron_BMI = round(BMI,2)
print(f"Chỉ số BMI là: {lam_tron_BMI}")
if BMI < 18.5:
    print("Bạn bị thiếu cân")
elif 18.5 <= BMI <= 24.9:
    print("Bạn có cân nặng bình thường")
elif 25 <= BMI <= 29.9:
    print("Bạn bị thừa cân")
else:
    print("Bạn bị béo phì")
    