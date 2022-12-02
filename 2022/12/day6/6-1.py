# 카렐 로봇 움직이기
# 벽이 랜덤으로 생성될 경우 어떻게 움직일 것인가
# 일부 움직임에 대해서는 기본적인 동작 함수가 구현되어 있다

# 적용 link : http://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Hurdle%204&url=worlds%2Ftutorial_en%2Fhurdle4.json


def turn_right():
    turn_left()
    turn_left()
    turn_left()
   
def jump():
    turn_left()
    while wall_on_right():
        move()
    turn_right()
    move()
    turn_right()
    while front_is_clear():
        move()
    turn_left()
    
while not at_goal():
    if wall_in_front():
        jump()
    else:
        move()