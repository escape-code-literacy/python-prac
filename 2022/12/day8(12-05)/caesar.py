# parameter : 함수에 호출되는 데이터의 이름
# argument : 그 데이터의 실제 값
# 위치 인자 : function(name, location) 으로 하면 첫 번째 위치의 argument가 name, 두 번째 위치의 argument가 location이 됨
# 키워드 인자 : function(location='seoul', name='choo')와 같이 하면 위치에 구애받지 않고 parameter에 argument를 할당
def encrypt(text, shift):
    
    # 알파벳 리스트 생성
    alphabet = []
    for x in range(ord('a'),ord('z')):
        alphabet.append(chr(x))
    
    # 입력받은 argument를 리스트로 변환
    text_list = list(text)
    
    # 문자 하나하나를 shift만큼 이동하여 해당 위치 문자로 치환
    for text in text_list:
        print(alphabet[(alphabet.index(text) + shift) % 26])
        text_list[text_list.index(text)] = alphabet[(alphabet.index(text) + shift) % 26]

    text = ''.join(text_list)
    print(f'the encoded text is {text}')
    
def decrypt(text, shift):
    
    # 알파벳 리스트 생성
    alphabet = []
    for x in range(ord('a'),ord('z')):
        alphabet.append(chr(x))
    
    # 입력받은 argument를 리스트로 변환
    text_list = list(text)
    
    # 문자 하나하나를 shift만큼 이동하여 해당 위치 문자로 치환
    for text in text_list:
        print(alphabet[(alphabet.index(text) - shift) % 26])
        text_list[text_list.index(text)] = alphabet[(alphabet.index(text) - shift) % 26]

    text = ''.join(text_list)
    print(f'the decoded text is {text}')


direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

if direction == 'encode':
    encrypt(text,shift)

else:
    decrypt(text,shift)

#TODO-1: Create a function called 'encrypt' that takes the 'text' and 'shift' as inputs.



    #TODO-2: Inside the 'encrypt' function, shift each letter of the 'text' forwards in the alphabet by the shift amount and print the encrypted text.  
    #e.g. 
    #plain_text = "hello"
    #shift = 5
    #cipher_text = "mjqqt"
    #print output: "The encoded text is mjqqt"

    ##HINT: How do you get the index of an item in a list:
    #https://stackoverflow.com/questions/176918/finding-the-index-of-an-item-in-a-list

    ##🐛Bug alert: What happens if you try to encode the word 'civilization'?🐛

#TODO-3: Call the encrypt function and pass in the user inputs. You should be able to test the code and encrypt a message. 