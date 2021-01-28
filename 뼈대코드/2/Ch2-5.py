# 실습 2-3코드를 함수로 개선

def fahrenheit2celsius(f):
    c = (f-32)*5/9
    return c


# Test code
print('''
Fahrenheit to Celsius conversion
Degrees in Fahrenheit?
''')
print(fahrenheit2celsius(67), "degrees in Celsius")
print(round(fahrenheit2celsius(67), 1), "degrees in Celsius")