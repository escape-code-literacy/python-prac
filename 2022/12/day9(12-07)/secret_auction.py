# 파이썬 딕셔너리 구조 및 리스트 중첩
# 비밀 경매 시스템 : 돌아가면서 본인의 이름과 입찰가를 입력한 후, 최고 입찰가를 제시한 사람 및 입찰가를 알려주는 시스템

print("Welcome to the secret auction program.")

# 플래그 생성
next_bidder = 'yes'
max_bid = 0
winner = ''
bid_list = {}

# 입찰자들이 순서대로 이름과 입찰가를 입력한다
while next_bidder == 'yes':
    name = input("What is your name? : ")
    bid = int(input("What's your bid?: $"))
    bid_list[name] = bid
    next_bidder = input("Are there any other bidders? Type 'yes' or 'no' : ")

# 입찰자 리스트에서 최고 금액과 대상 입찰자를 추출한다
for name, bid in bid_list.items():
    if bid > max_bid:
        max_bid = bid
        winner = name

print(f'The winner is {winner} with a bid of {max_bid}')
