# 행맨 게임 개발을 위해 구조 설계

# 1. 단어를 랜덤으로 뽑는다
# 2. 단어를 ----의 형태로 보여준다
# 3. 유저가 알파벳을 하나씩 말한다
# 4. 분기 처리 -> 단어에 알파벳이 있을 시 알파벳 위치의 -를 알파벳을 바꾼다 / 없을 시 행맨을 하나씩 그린다
# 5. 행맨이 다 그려지면 게임 오버 (WIN) / 알파벳이 다 완성되면 게임 오버 (LOSE)

#Step 1 -> 무작위 단어를 고르고 알파벳 넣어보기
import random
import hangman_words

stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

#TODO-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word.
chosen_word = random.choice(hangman_words.word_list)
print(chosen_word)

# display word list 생성
underbar = []
for _ in range(len(chosen_word)):
    underbar.append('-')


death_count = 6
underbar_count = len(chosen_word)

print(stages[death_count])

#TODO-2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercas
while '-' in underbar:
    user_guess = input("what's the letter of word chosen?? : ").lower()
   
      
    # if guess already exists, continue  
    if user_guess in underbar:
            print(f"You've already guessed {user_guess}")
            continue 
  
          
    #TODO-3 - Check if the letter the user guessed (guess) is one of the letters in the chosen_word.
    for i in range(len(chosen_word)):
        if user_guess == chosen_word[i]:
            underbar[i] = user_guess
   
            
    # if guess incorrect, 1 life out
    if user_guess not in underbar:
        death_count -= 1
        print(stages[death_count])
    
    print(''.join(underbar))   
  
    
    # if 0 life, game over
    if death_count == 0:
        print("Game Over")
        break



if death_count != 0:
    print("WIN")

           
