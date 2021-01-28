
#  변수 = (람다식) : bady
#  꼴로 함수식을 만들수 있다. => 람다 요약이라고 한다.

from math import pi
area_circle = lambda radius: pi * radius ** 2
print(area_circle(3))
print(area_circle(5))
print(area_circle(9))