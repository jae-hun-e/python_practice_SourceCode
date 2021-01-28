# 람다 요약은 널리 필요한 프로그램 구조이기 때문에 정의하는 형식이 따로 있다.
# 이 식을 정의하는 형식을 함수 정의라고 한다.

from math import pi

def area_circle(radius):  # def 함수이름(변수): 꼴로 함수정의를 해준다. => 람다식의 파라미터
	return pi * radius ** 2  # return 값으로 함수의 식을 나타낸다. => bady

print(area_circle(3))



# from math import pi
#
# def area_circle(radius):
# 	return pi * radius ** 2
#
# print(area_circle(3))
# print(area_circle(5))
# print(area_circle(9))