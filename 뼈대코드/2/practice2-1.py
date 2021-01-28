# 온도 변환 함수

def celsius2fahrenheit (c) :
    return round(c*9/5 + 32, 2)

# test code
print(celsius2fahrenheit(19.4))  #66.92
print(round(celsius2fahrenheit(19.4), 1))  #66.9