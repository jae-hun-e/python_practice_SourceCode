# 대출 원리금 균등분할 상환금 계산

def monthly_payment_plan(principal, interest, year) :
    p = principal
    r = interest/100/12
    m = year*12
    total = ((1+r)**m * p * r) / ((1+r)**m - 1)  # 괄호 주의!!!!
    return int(total)


print("""
자유은행 대출 상환금 계산 서비스에 오심을 환영합니다.
대출원금이 얼마인가요? (백만원 이상)""")
p = int(input())


print("연 이자율은 몇%인가요?(0.0~9.9) ")
i = float(input())

print("상환기간은 몇 년인가요? ")
y = int(input())

print("""
대출 상환금 내역을 알려드리겠습니다.
대출원금:""", p, "연 이자율", i, "매월", monthly_payment_plan(p,i,y), """원씩 지불하셔야 합니다.
상환 완료시까지 총 상환금액은 """, monthly_payment_plan(p,i,y) * 12 * y, "원입니다.")
print("저희 자유은행은 항상 여러분과 함께 합니다.\n\
또 들려주세요.")
