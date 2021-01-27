# 타입 변환 이해

int(7)
int(0.1)
int(3.84)
int(0.2e3)
int("2020")
int("3.14")  # 안됨 int(float("3.14"))라고 해야됨 -> int는 정수 형태를 제대로 갖춘 문자열만 정수로 변환
int("3+4")  # +기호는 int형으로 못바꿈 int(str(int(3+4)))로 해야함 -> 위와 동일
int("three")  # 응 안돼

float(3)
float(3.14)
float("3.14")
float("3")
float("0.1*0.1")  # 못바꿈

str(2018)
str(3+4)
str(1.414)
str(0.1*0.1)
str(3.14e-3)