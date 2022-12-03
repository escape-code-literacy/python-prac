"""
    어떤 숫자가 주어졌을 때 각 자리수의 합이 소수인지 판별하는 함수 구현
    Problem directed by Kimdongui
    Solver : Choo
"""

# TODO : 함수 구현하기
def func(number):
    answer = True
    
    # Calculate sum of each digit
    a = str(number)
    result = 0
    for i in a:
        result = result + int(i)

    # 소수 판별 : 2부터 제곱근의 수까지(제곱근이 약수의 중간값에 해당하기 때문) 중 하나라도 나누어 떨어지면 False를 반환하도록 동작
    for j in range(2,int(result**0.5)+1):
        if result % j == 0:
            answer = False
            break
        
    return answer

print(func(125))


