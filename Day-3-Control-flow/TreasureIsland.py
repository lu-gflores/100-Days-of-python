print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 

direction = input('You find yourself at a crossroad, which path do you take? Left or Right? ')

if direction.lower() == 'left':
  swim_wait = input('You stumble at a lake with a tower in view. A boat may yet arrive, but you try to swim across. Swim or Wait? ')
  if swim_wait.lower() == 'wait':
    door_color = input('You arrive and enter the tower. You see a Red door, a Blue Door, and a Yellow door. Which door do you enter? Red, Blue, or Yellow? ')
    if door_color.lower() == 'red':
      print('Upon opening the red door, a dragon breaths fire and roasts you. GAME OVER.')
    elif door_color.lower() == 'blue':
      print("Upon opening the blue door, you are pulled in by a winter's breath and the door behind you freezes shut. You are trapped in the a frozen plain. GAME OVER.")
    elif door_color.lower() == 'yellow':
      print('Upon opening the yellow door, you find a treasure chests and mountains of gold surroudning it. You win!')
    else:
      print('You decide to leave the tower and wait for the boat to arrive to take you home. GAME OVER.')
  else:
    print('You were attacked by a man eating trout. GAME OVER.')
else:
  print("You chose the right path...which lead to a bear cave with you in the bear's sight. GAME OVER.")

