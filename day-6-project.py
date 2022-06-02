##REEBORG NAVIGATES MAZE

def turn_right():
    turn_left()
    turn_left()
    turn_left()

        
while not at_goal(): 
    if right_is_clear():
        turn_right()
    while front_is_clear():
        move()
    else:
        turn_left()
   
#return after day-15 to refine code logic
