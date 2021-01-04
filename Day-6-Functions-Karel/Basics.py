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