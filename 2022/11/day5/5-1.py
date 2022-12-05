# 반복문을 사용해서 리스트 내 최댓값 구하기

student_scores = input("Input a list of student scores: ").split()

for i in range(len(student_scores)):
    student_scores[i] = int(student_scores[i])

max_num = 0

for score in student_scores:
    if score > max_num:
        max_num = score

print(f'The highest score in the class is: {max_num}')
print(max(student_scores))