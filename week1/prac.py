"""
    어떤 숫자가 주어졌을 때 각 자리수의 합이 소수인지 판별하는 함수 구현
    Problem directed by Kimdongui
    Solver : Choo
"""

def func(number):
    """
        func(123) -> False
        func(11) -> True
        func(171) -> False
        func(1006) -> True
    """
    #TODO : 함수 구현하기
    answer = None

    # a = str(number)
    # result = 0
    # for i in a:
    #     result = result + int(i)

    while  (number / 10) > 0 :



        number = number / 10

    count = 0

    for j in range(2,result):
        if result % j == 0:
            count = count + 1

    if count > 0:
        answer = False

    else:
        answer = True
        
    return answer

print(func(128))

