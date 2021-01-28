# 9의 보수 계산 함수
# 보수란 각 자리 수에서 9와의 차이로 얻는 수이다.
# 보수구하는 식
# 자연수n의 자리 수를 k라고 하면
# n에 대한 0의 보수는 10^k -1 -n이다.
# 자리수를 아는방법은 내장함수 len으로 구할 수있다.
# len("342) => 3
# 함수명은 complement_none으로 해라.

def complement_none(n):
    k = len(str(n))
    return 10**k - 1 - n




# test code
print(complement_none(0))  #9
print(complement_none(9))  #0
print(complement_none(4))  #5
print(complement_none(18))  #81
print(complement_none(40))  #59
print(complement_none(307))  #692
print(complement_none(9142))  #857
print(complement_none(9965))  #34
print(complement_none(9999))  #0