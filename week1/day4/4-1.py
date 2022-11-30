# 사람들 중 랜덤으로 계산할 사람 고르기
# input으로 받아온 결과를 ',' 구분자를 바탕으로 split -> list 형태로 반환됨


import random

names_string = input("Give me everybody's names, seperated by a comma.\n")
names = names_string.split(',')
print(names)

random_name = random.choice(names)
print(f'{random_name} is going to buy the meal today!')