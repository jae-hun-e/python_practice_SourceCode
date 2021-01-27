# 동진 합산 서비스
#
# 액면가가 큰 동전부터 순서대로 보유 동전의 개수를 입력받고 실행결과가
# Enter the number of coins you have.
# 500 won? 4
# 100 won? 2
#  50 won? 2
#  10 won? 1
# you have 2310 won in total.
# 처럼 나와야 한다.

print("Enter the number of coins you have.")
print("500 won? ")
a = int(input())
print("100 won? ")
b = int(input())
print(" 50 won? ")
c = int(input())
print(" 10 won? ")
d = int(input())
sum = 500*a + 100*b + 50*c + 10*d
print("you have", sum, "won in total.")

