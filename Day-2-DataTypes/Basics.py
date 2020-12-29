#Data Types
# prints 'o'  
print('Hello'[4])

#Integers
print( 123 + 456)

123_123_342

#Float
3.145855

#Boolean
True
False

# num_char = len(input('What is your name?'))
# new_num_char = str(num_char)
# print('Your name has ' + new_num_char + ' characters.')

# a = float(13)
# print(type(a))
# print(70 + float('100.5'))

# PEMDASLR
# Parenthesis, Exponents, Division, Addition, Subtraction
# Goes left to right
# ()
# **
# * /
# + -
print( 3 / 3 * 3 + 3 - 3)

# rounds to 2 decimal places
print( round(8 / 3, 2) )

# floor division converts to integer
print( 8 // 3)

score = 0
height = 1.8
isWinning = True
# user scores a point (can short hand)
score = score + 1
score += 1

#f-string 
print(f'Your score is {score}, your height is {height}, you are winning is {isWinning}')

# 2-1 Exercise
# 🚨 Don't change the code below 👇
two_digit_number = input("Type a two digit number: ")
# 🚨 Don't change the code above 👆

####################################
#Write your code below this line 👇


first = int(two_digit_number[0])
second = int(two_digit_number[1])

two_digit_number = first + second
print(two_digit_number)




# 2-2 Exercise
# 🚨 Don't change the code below 👇
height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

result = int(weight) / (float(height) ** 2)
print(int(result))



# 2-3 Exercise
# 🚨 Don't change the code below 👇
age = input("What is your current age?")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
days = (90 * 365)- int(age) * 365
weeks = (90 * 52) - int(age) * 52
months = (90 * 12) - int(age) * 12

print(f"You have {days} days, {weeks} weeks, and {months} months left.")