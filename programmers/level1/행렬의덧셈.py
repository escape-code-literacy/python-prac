# 문제 설명
# 행렬의 덧셈은 행과 열의 크기가 같은 두 행렬의 같은 행, 같은 열의 값을 서로 더한 결과가 됩니다. 2개의 행렬 arr1과 arr2를 입력받아, 행렬 덧셈의 결과를 반환하는 함수, solution을 완성해주세요.

# 제한 조건
# 행렬 arr1, arr2의 행과 열의 길이는 500을 넘지 않습니다.
# 입출력 예
# arr1	arr2	return
# [[1,2],[2,3]]	[[3,4],[5,6]]	[[4,6],[7,9]]
# [[1],[2]]	[[3],[4]]	[[4],[6]]

def solution(arr1, arr2):
    answer = []
    temp = []
    
    for i in range(len(arr1)):
        for j in range(len(arr1[0])):
            temp.append(0)
        
        answer.append(temp)
        temp = []
    
    for i in range(len(arr1)):
        for j in range(len(arr1[0])):
            answer[i][j] = arr1[i][j] + arr2[i][j]
    return answer

    # Feedback
    # 다른 사람의 풀이를 참조했을 때 행렬의 덧셈 반복문을 아예 처음부터 매트릭스 안에서 돌렸다.
    # 대표적인 예시가 
    # answer = [[c+d for c,d in zip(a,b)] a,b in for arr1,arr2]
    # 이 미친사람은 한 문장으로 풀었다.
    # 여기서 극강의 효율을 자랑하는 zip함수란 동일한 갯수의 자료형에 대해
    # 인덱스 위치가 동일한 순서끼리 묶어주는 것이다.
    # 따라서 양 행렬의 행(a,b) 요소들에 대해 열 값(c,d)들을 더해준 걸 매트릭스 내에 적재한다.