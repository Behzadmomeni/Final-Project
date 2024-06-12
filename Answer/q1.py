## تابع کانوولوشن یک بعدی که آرگومان های سیگنال و فیلتر رو به عنوان آرگومان دریافت میکنه
def convol(signal, filter):
    result = [0] * (len(signal) + len(filter) - 1)
    
    for i in range(len(signal)):
        for j in range(len(filter)):
            result[i + j] += signal[i] * filter[j]
    
    return result

## دریافت طول سیگنال
signal_len = input("please input the signal len: ")
signal = []
filter = []

## مقدار دهی آرایه سیگنال
for i in range(0, int(signal_len)):
    signal.append(input(f"input the {i+1} member of signal: "))

## دریافت طول آرایه فیلتر
filter_len = input("please input the filter len: ")

## مقدار دهی آرایه
for i in range(0, int(filter_len)):
    filter.append(input(f"input the {i+1} member of filter: "))

## کست کردن به اینت
for i in range(0, len(signal)):
    signal[i] = int(signal[i])

for i in range(0, len(filter)):
    filter[i] = int(filter[i])

## اجرای کانوولوشن روی ورودی و پرینت خروجی
res = convol(signal, filter)
print("Convolution Result:", res)

## ذخیره در فایل برای بازبینی های بعدی
with open("1.txt", "a") as file:
    file.write(f"{res}\n")
