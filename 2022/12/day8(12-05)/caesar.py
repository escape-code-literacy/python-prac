# parameter : 함수에 호출되는 데이터의 이름
# argument : 그 데이터의 실제 값
# 위치 인자 : function(name, location) 으로 하면 첫 번째 위치의 argument가 name, 두 번째 위치의 argument가 location이 됨
# 키워드 인자 : function(location='seoul', name='choo')와 같이 하면 위치에 구애받지 않고 parameter에 argument를 할당

# 카이사르 암호(Caesar_cipher) : 문자열의 각 알파벳을 입력한 n회 뒤로 shift하여 암호화 및 n회 앞으로 shift하여 복호화하는 암호 방식
# ex) abcde를 5만큼 뒤로 shift하여 encoding하면 fghij, fghij를 5만큼 앞으로 shift하여 decoding하면 abcde가 된다

def caesar_cipher(text, shift_amount, cipher_direction):
    
    # 알파벳 리스트 생성
    alphabet = []
    for x in range(ord('a'),ord('z')+1):
        alphabet.append(chr(x))
    
    # 입력받은 argument를 리스트로 변환
    text_list = list(text)
    
    # 문자 하나하나를 shift만큼 이동하여 해당 위치 문자로 치환
    if cipher_direction == 'decode':
        shift_amount *= -1

    # 문자열의 요소가 알파벳인 경우 shift_amount만큼 앞 또는 뒤로 shift함. z에서 넘어가는 경우 a로 돌아가도록 처리 
    for i in range(len(text_list)):
        if text_list[i] in alphabet:
            text_list[i] = alphabet[(alphabet.index(text_list[i]) + shift_amount) % 26]

    text = ''.join(text_list)
    print(f'the {cipher_direction}d text is {text}')
    
choose = 'yes'

# 암호화를 계속해서 시도할 수 있게 하는 반복 구문
while choose == 'yes':
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt: ")
    input_text = input("Type your message: ").lower()
    shift = int(input("Type the shift number: "))

    caesar_cipher(shift_amount = shift, text = input_text, cipher_direction = direction)

    # 암호화를 계속 시도할지 말지 결정하는 플래그
    choose = input("Type 'yes' if you want to go again, Otherwise type 'no': ")

    if choose == 'no':
        print('Goodbye')

