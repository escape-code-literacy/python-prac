"""
    어떤 숫자가 주어졌을 때 각 자리수의 합이 소수인지 판별하는 함수 구현
    Problem directed by Kimdongui
    Solver : Choo
"""

def func(number):
    # TO-DO : 함수 구현하기
    answer = None

    a = str(number)
    result = 0
    for i in a:
        result = result + int(i)

    count = 0

    for j in range(2,result):
        if result % j == 0:
            count = count + 1

    if count > 0:
        answer = False

    else:
        answer = True
        
    return answer

print(func(124))

