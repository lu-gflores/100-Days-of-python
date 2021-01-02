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

