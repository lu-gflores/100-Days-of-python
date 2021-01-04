#Making our own functions
#Defining functions

#def my_funciton():
  #Do this
  #Then this
  #And this

def my_function():
  print('Hey there')
  print('Goodbye')
my_function()

# while loop
while something_is_true:
    #Do this
    #then this
    #etc...

number_of_hurdeles = 6

#loops through number of hurdles while this condition is true
while number_of_hurdeles > 0:
    number_of_hurdeles =-1
    print(number_of_hurdeles)



##Exercies are from the Reeborg's world site 
# 6 - 1 Make a square
def turn_around():
    turn_left()
    turn_left()
    turn_left()
#Draw Square  
turn_left()
move()
turn_around()
move()
turn_around()
move()
turn_around()
move()


# 6 - 2 Jumping Hurdles
def turn_around():
    turn_left()
    turn_left()
    turn_left()
    
def jump():
    move()
    turn_left()
    move()
    turn_around()
    move()
    turn_around()
    move()
    turn_left()

for num in range(6):
    jump()

#will loop until jump is equal to at_goal()
while not at_goal():
    jump()


# 6- 3 randomized hurdle jumping
def turn_around():
    turn_left()
    turn_left()
    turn_left()
    
def jump():
    turn_left()
    move()
    turn_around()
    move()
    turn_around()
    move()
    turn_left()
    
while not at_goal():
    if wall_in_front():
        jump()
    else:
        move()

# 6 - 4 Advanced randomized hurdle jumpoing

def turn_around():
    turn_left()
    turn_left()
    turn_left()
    
def jump():
    turn_left()
    while wall_on_right():
        move()
    turn_around()
    move()
    turn_around()
    while front_is_clear():
        move()
    turn_left()
    
while not at_goal():
    if wall_in_front():
        jump()
    else:
        move()
# Escaping the Maze
def turn_right():
    turn_left()
    turn_left()
    turn_left()

    
while not at_goal():
    if right_is_clear():
        turn_right()
        move()
    elif not front_is_clear():
        turn_left()
    elif front_is_clear():
        move()