# 동전 합산 함수
# 실습 2-2를 함수로 만들어라.
# 키보드 입력 대신 각 동전의 개수를 인수로 받아서 총액을 계산해주는 함수의 이름을
# coin_in_total이라고 해라.

def coin_in_total(c500, c100, c50, c10) :
    return c500*500 + c100*100 + c50*50 +c10*10

print("Enter the number of coins you have.")
print("500 won? ")
a = int(input())

print("100 won? ")
b = int(input())

print("100 won? ")
c = int(input())

print("100 won? ")
d = int(input())


print("You have", coin_in_total(a, b, c, d), "won in total")