# 키보드 입력과 반올림
# 원의 면적계산 결과 소수 첫째 자리에서 반올림
# ex : The area of a circle with radius 3.0 is 28.3

radius = float(input())

from math import pi
area = pi * radius ** 2
print("The area of a circle with radius", radius, "is", round(area))
