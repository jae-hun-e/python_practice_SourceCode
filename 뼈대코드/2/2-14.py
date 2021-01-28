from math import pi

def area_circle(radius): 
	area = pi * radius ** 2
	return round(area, 2)  # 소수점 둘째 자리까지 반올림해서 나타냄

print(area_circle(3))
print(area_circle(5))
print(area_circle(9))