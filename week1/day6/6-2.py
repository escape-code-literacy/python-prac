# 미로 빠져나가기 (미로는 그대로이나 로봇의 위치 및 방향이 랜덤으로 생성됨)
# 길을 잃었으면 항상 오른쪽 벽을 따라 가되 오른쪽이 막혀 있으면 직진, 둘 다 안되면 최후의 수단으로 왼쪽으로 향해서 미로를 탈출한다

# link : https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Maze&url=worlds%2Ftutorial_en%2Fmaze1.json

def turn_right():
    turn_left()
    turn_left()
    turn_left()
    
  

while not at_goal():
    if right_is_clear():
        turn_right()
        move()
    
    elif wall_on_right():
        if wall_in_front():
            turn_left()
        
        else:
            move()

# 이 경우 특정 위치에서 무한 루프에 빠질 수 있다. 추후 해당 부분에 대해 디버깅을 진행할 예정