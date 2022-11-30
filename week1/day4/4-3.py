import random

choose = int(input("what do you choose? Type 0 for Rock, 1 for paper or 2 for Scissors\n"))

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

groups = [rock,paper,scissors]
yours = groups[choose]
print(yours)

computer_chose = random.choice(groups)
print(f"Computer chose:")
print(computer_chose)

if yours == rock:
    if computer_chose == paper:
        print("You Lose")
    
    elif computer_chose == scissors:
        print('You Win!')

    else:
        print("draw")

elif yours == paper:
    if computer_chose == scissors:
        print("You Lose")
    
    elif computer_chose == rock:
        print('You Win!')

    else:
        print("draw")

else:
    if computer_chose == rock:
        print("You Lose")
    
    elif computer_chose == paper:
        print('You Win!')

    else:
        print("draw")    
