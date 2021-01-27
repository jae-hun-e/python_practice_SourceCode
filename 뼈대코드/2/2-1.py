# 한줄 주석 , 단축키 ctrl + /

"""
이것도 여러줄 주석
"""
# 1 필요한 상수만 불러옴

radius = 25.365
from math import pi

area = pi * radius ** 2
print(area)

# 2 전체풀러와서 필요한 상수 사용

import math

pi = math.pi
area2 = pi * radius ** 2
print(area2)
