from math import pi

def area_circle(radius, n): 
	area = pi * radius ** 2
	return round(area, n)  # 소수점 몇번째 자리까지 나타낼지를 인수로 받음

print(area_circle(3, 1))
print(area_circle(5, 2))
print(area_circle(9, 3))