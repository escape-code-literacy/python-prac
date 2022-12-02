# 파이썬은 매 변수 생성시마다 객체를 생성해 할당한다.
# 그렇게 되면 객체 수가 늘어나 시스템적으로 많은 비용이 할당된다.
# 그래서 일정 숫자까진 자주 사용되는 객체를 하나 미리 생성해 놓는다.

def check():
    for x in range(-260,260):
        for y in range(x,x+1):
            if id(x)==id(y):
                print("%d는 미리 생성된 객체" % x)
            else:
                print("%d는 새롭게 만들어진 객체" % x)

check()

# -5~256까진 id가 모두 동일하다. 즉, 동일한 주소로 메모리 공간을 참조한다.