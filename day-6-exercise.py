##1.0 REEBORG - MOVE IN A SQUARE
def turn_around():
    turn_left()
    turn_left()

def turn_right():
    turn_around()
    turn_left()

turn_left()
move()
turn_right()
move()
turn_right()
move()
turn_right()
move()

##2.0 REEBORG - HURDLE

def jump():
    move()
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()
    
jump()
jump()
jump()
jump()
jump()
jump()

#or

for step in range(6):
  jump()

#or

number_of_hurdles = 0 
while number_of_hurdles > 0:
  jump()
  number_of_hurdles -= 1


##3.0 REEBORG - RANDOM HURDLE GOAL

while not at_goal():
    jump()

#or


while at_goal() != True:
    jump()

#or
    
while not at_goal() == True:
    if front_is_clear():
        move()
    if wall_in_front():
        jump()

##4.0 REEBORG - RANDOM HURDLE HEIGHT
#shows a detailed way of how while loops can be used

def turn_around():
    turn_left()
    turn_left()

def turn_right():
    turn_around()
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
        
def fall():
    move()
    
while not at_goal():
    if front_is_clear():
        move()
    if wall_in_front():
        jump()