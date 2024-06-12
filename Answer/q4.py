from math import *
import json

pw = input("power :")
pw = float(pw)

Density = input("density :")
Density = float(Density)

v1 = input("v1 :")
v1 = float(v1)

v2 = input("v2 :")
v2 = float(v2)

core_A = round(pw / (Density * v2), 4)

r1 = round(v1 / sqrt(2), 4)
r2 = round(v2 / sqrt(2), 4)

print(f"Core area: {core_A}")
print(f"turns in p_coil: {r1}")
print(f"turns in s_coil: {r2}")

## ذخیره در فایل
data = {
    "core_area": core_A,
    "primary_rounds": r1,
    "secondary_rounds": r2
}

with open("4.txt", "a") as file:
    file.write(f"{json.dumps(data)}\n")
