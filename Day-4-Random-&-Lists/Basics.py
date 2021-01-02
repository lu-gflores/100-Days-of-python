#importing random module 
# import random

# #imports my_moduel.py file
# import my_moduel

# ##generates a random number 1 to 10
# random_integer = random.randint(1, 10)
# print(random_integer)


# ## prints the variable of pi form the file
# print(my_moduel.pi)

# # 0.0000 to 0.999999999.....
# random_float = random.random()
# print(random_float)

# random_float * 5

# love_score = random.randint(1, 100)
# print(f'your love score is {love_score}')

# Lists

states = ['Delaware', 'South Carolina', 'New York', 'Nevada']
# prints New york
print(states[2])
# prints the last item in the list!

print(states[-1])
# updates south carolina
states[1] = 'North Carolina'

# adds and element at the end of the list
states.append('Finland')

# adds items in the list
states.extend(['Georgia', 'Rhode Island'])
print(states)

# results in error since index is out of range
print(states[23])

# 4 - 1 Exercise
import random

coin = random.randint(0, 1)

if coin == 1:
  print(f'Heads')
else:
  print(f'Tails')

# 4 -2 Exercise
# # Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆
import random
#Write your code below this line 👇

length_names = len(names)
random_person = random.randint(0, length_names - 1)
paying_person = names[random_person]

print(f'{paying_person} will be covering the meal!')


# 4- 3

# 🚨 Don't change the code below 👇
row1 = ["⬜️","⬜️","⬜️"]
row2 = ["⬜️","⬜️","⬜️"]
row3 = ["⬜️","⬜️","⬜️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ")
# 🚨 Don't change the code above 👆

#Write your code below this row 👇

col = int(position[0]) - 1
row = int(position[1]) - 1

map[row][col] = 'X'


#Write your code above this row 👆

# 🚨 Don't change the code below 👇
print(f"{row1}\n{row2}\n{row3}")

