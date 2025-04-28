# https://reeborg.cs20.ca/?lang=en&mode=python&menu=%2Fworlds%2Fmenus%2Fsk_menu.json&name=Maze&url=%2Fworlds%2Ftutorial_en%2Fmaze1.json
#Either the test front_is_clear() or
#wall_in_front(), right_is_clear() or
#wall_on_right(), and at_goal()

def turn_right():
    turn_left()
    turn_left()
    turn_left()
 
#this loop is tricky 
while front_is_clear():
    move()
turn_left()

while at_goal() != True:
    if right_is_clear():
        turn_right()
        move()
    elif front_is_clear():
        move()
    else:
        turn_left()