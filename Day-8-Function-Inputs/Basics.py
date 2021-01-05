# Review: 
# Create a function called greet(). 
# Write 3 print statements inside the function.
# Call the greet() function and run your code.


def greet():
  print('Hey there')
  print('My name is George')
  print('And I am a developer')
greet()


#function with input
def greet_name(name):
  print(f'Hey {name}')
  print(f'How are you {name}?')
  print(f'And I am a developer')
greet_name('Johnny')

def greet_with(name, location):
  print(f"Hey there {name}")
  print(f"You live in {location}")
greet_with(location = 'Nowhere', name='Dave')


# Exercises

# 8-1
#Write your code below this line 👇

import math

def paint_calc(height, width, cover):
  num_of_cans = math.ceil((height * width) / cover)
  print(f"You'll need {num_of_cans} cans of paint.")




#Write your code above this line 👆
# Define a function called paint_calc() so that the code below works.   

# 🚨 Don't change the code below 👇
test_h = int(input("Height of wall: "))
test_w = int(input("Width of wall: "))
coverage = 5
paint_calc(height=test_h, width=test_w, cover=coverage)


# 8-2 
#Write your code below this line 👇

def prime_checker(number):
  isPrime = True
  for i in range(2, number):
    #Not a prime number
    if number % i == 0:
      isPrime = False
  if isPrime:
    print("It's a prime number.")
  else:
    print("It's not a prime number.")


#Write your code above this line 👆
    
#Do NOT change any of the code below👇
n = int(input("Check this number: "))
prime_checker(number=n)



