# 온도 변환 서비스
# 화씨를 섭씨로 바꿔라.
# 섭씨 = (화씨-32)*5/9


print('''
Fahrenheit to Celsius conversion
Degrees in Fahrenheit?
''')
F = float(input())
c = (F-32)*5/9
print(round(c, 1), "degrees in Celsius")
