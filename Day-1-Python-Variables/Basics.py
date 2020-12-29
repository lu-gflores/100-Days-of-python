#input() will get user input in console
# Then print() will print the word 'Hi' and the user input

#print('Hi ' + input('What is your name?') + '!')

## 1-2 Exercise
print("Day 1 -" + " String Manipulation")
print('String Concatenation is done with the "+" sign.')
print('e.g. print("Hello " + "world")')
print("New lines can be created with a backslash and n.")

## 1-3 Exercise
##nests the input function within the length function to print the length of 
## characters
print(len(input('What is your name? ')))

## 1-4 Exercise 

# declaring a variable to name
name = "jack"
print(name)

name = 'jill'
print(name)

name = input('What is your name? ')
length = len(name)
print(length)

## 1- 5 Exercise Swapping values 
# 🚨 Don't change the code below 👇
a = input("a: ")
b = input("b: ")
# 🚨 Don't change the code above 👆

####################################
#Write your code below this line 👇
c = a
a = b
b = c


#Write your code above this line 👆
####################################

# 🚨 Don't change the code below 👇
print("a: " + a)
print("b: " + b)

