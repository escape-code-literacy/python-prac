# 무작위 암호 설정하기

import random

# letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
letters = ''
# 소문자 아스키코드 변환하여 문자열 생성
for i in range(97,123):
    letters += chr(i)
    
# 대문자 아스키코드 변환하여 문자열 생성
for I in range(65,91):
    letters += chr(I)

# numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
numbers = ''
# 0 ~ 9 문자열 생성
for num in range(0,10):
    numbers += str(num)


# symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
symbols = ''
# 특수 문자 아스키코드 변환하여 문자열 생성
for x in range(33,44):
    if x == 34 or x == 39:
        continue
    symbols += chr(x)

print(letters)
print(numbers)
print(symbols)
print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

Pypassword = ''

for i in range(nr_symbols):
    Pypassword += random.choice(letters)

for i in range(nr_letters):
    Pypassword += random.choice(symbols)

for i in range(nr_numbers):
    Pypassword += random.choice(numbers)

print(f"Your password is {Pypassword}!")

