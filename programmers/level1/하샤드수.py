# 문제 설명
# 양의 정수 x가 하샤드 수이려면 x의 자릿수의 합으로 x가 나누어져야 합니다. 예를 들어 18의 자릿수 합은 1+8=9이고, 18은 9로 나누어 떨어지므로 18은 하샤드 수입니다. 자연수 x를 입력받아 x가 하샤드 수인지 아닌지 검사하는 함수, solution을 완성해주세요.

# 제한 조건
# x는 1 이상, 10000 이하인 정수입니다.
# 입출력 예
# arr	return
# 10	true
# 12	true
# 11	false
# 13	false
# 입출력 예 설명
# 입출력 예 #1
# 10의 모든 자릿수의 합은 1입니다. 10은 1로 나누어 떨어지므로 10은 하샤드 수입니다.

# 입출력 예 #2
# 12의 모든 자릿수의 합은 3입니다. 12는 3으로 나누어 떨어지므로 12는 하샤드 수입니다.

# 입출력 예 #3
# 11의 모든 자릿수의 합은 2입니다. 11은 2로 나누어 떨어지지 않으므로 11는 하샤드 수가 아닙니다.

# 입출력 예 #4
# 13의 모든 자릿수의 합은 4입니다. 13은 4로 나누어 떨어지지 않으므로 13은 하샤드 수가 아닙니다.


# 기존 자릿수 합을 구하는 솔루션1
def solution1(x):
    answer = True
    number = 0
    temp = x
    
    while x > 10:
        number += (x % 10)
        print(number)
        x = x // 10
        print(x)
    
    number += x
    print(temp)
    
    if temp % number != 0:
        answer = False
  
    return answer

# 기존 자릿수 합을 구하는 솔루션2
def solution2(x):
    answer = True
    number = sum(map(int, str(x)))
    print(number)
    
    if x % number != 0:
        answer = False
  
    return answer

def solution3(x):
    answer = True

    # 원리1 - join 함수 : join은 iterable 객체를 .앞의 인자를 넣어서 합쳐 문자열로 반환함. 주로 ''.join(list)와 같이 list를 인자 없이 합쳐 문자열로 반환하는데 씀
    # 원리2 - eval 함수 : eval은 문자열로 연산을 가능하게 하는 함수 ex) eval('1+2') = 3 이라는 결과가 나온다 
    number = eval('+'.join(str(x)))
    print(number)

    if x % number != 0:
        answer = False
  
    return answer


print(solution1(11))
print(solution2(11))
print(solution3(11))