import math
import json


## تابع اصلی
## مسئول دریافت ماتریس زمین بازی و محاسبه میدان الکتریکی
def main():
	height = input("input height of array ")
	width = input("input width of array ")
	height = int(height)
	width = int(width)
	x_e = 0
	y_e = 0
	t_height = -1
	t_width = -1
	arr = [[0 for x in range(int(width))] for y in range(int(height))]
	for i in range(0, height):
		for j in range(0, width):
			arr[i][j] = input(f"please input the value for cell {i + 1} {j + 1} ")
			## تایید نقطه مرجع
			if arr[i][j].lower() == "o":
				t_height = i
				t_width = j

	## چک کردن وجود نقطه مرجع
	if t_height == -1 or t_width == -1:
		print("I didnt found any \'O\' in your input")
		main()

	## محاسبه میدان در هر راستا
	for i in range(0, height):
		for j in range(0, width):
			if i == t_height and j == t_width:
				continue
			else:
				r = math.sqrt((i - t_height) **2 + (j - t_width) **2)
				if r == 0:
					continue
				p_e = int(arr[i][j]) / (r **2)
				x_e += p_e * ((i - t_height) / r)
				y_e += p_e * ((j - t_width) / r)

	## ذخیره در فایل و نمایش خروجی
	print()
	print(x_e, y_e)
	print(f"X:K*{x_e} Y:K*{y_e}")
	data = {
		"arr" : arr,
		"p_e" : p_e,
		"x_e" : x_e,
		"y_e" : y_e
	}
	print(data)
	with open("2.txt", "a") as file:
		file.write(f"{json.dumps(data)}\n")

main()