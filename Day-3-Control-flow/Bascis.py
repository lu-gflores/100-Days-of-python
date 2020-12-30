print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))

bill = 0

# if else statement
if height >= 120:
  print('YOu can ride the rollercoaster!')
  #nested if/else
  age = int(input('What is your age? '))
  if age < 12:
    bill = 5
    print('Child tickets are $5.')
  elif age <= 18:
    bill = 7
    print('Youth Tickets are $7.')
  
  #logical operator
  elif age >= 45 and age <= 55:
    print('Have a mid-life crisis? Free ride for you!')
  
  else:
    bill = 12
    print('Adult Tickets are $12.')
  
  wants_photo = input('Do you want a photo taken? Y or N. ')
  if wants_photo == 'Y':
    # Adds $3 to their bill
    bill += 3
  print(f'Your final bill is ${bill}')

else :
  print('Sorry, you have to grow a bit taller...')

# Exercises below


# 3 - 1  odd or even?

number = int(input("Which number do you want to check? "))

if number % 2 == 0:
  print('This is an even number.')
else:
  print('This is an odd number.')

#3 - 2 BMI Revisted

height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))

bmi = round(weight / (height ** 2))

if bmi < 18.5:
  print(f'Your BMI is {bmi}, you are underweight.')
elif bmi < 25:
  print(f'Your BMI is {bmi}, you have a normal weight.')
elif bmi < 30:
  print(f'Your BMI is {bmi}, you are overweight.')
elif bmi < 35:
  print(f'Your BMI is {bmi}, you are obese')
else:
  print(f'Your BMI is {bmi}, you are clinically obese.')

# 3 - 3 Leap year

year = int(input("Which year do you want to check? "))

if year % 4 == 0:
  if year % 100 !=0:
    print('Leap year.')
  elif year % 400 == 0:
    print('Leap year.')
  else:
    print('Not leap year.')
else:
  print('Not leap year.') 

# 3 - 4 Pizza order
# 🚨 Don't change the code below 👇
print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

bill = 0

if size == 'S':
  bill = 15
  if add_pepperoni == 'Y':
    bill += 2
  if extra_cheese == 'Y':
    bill += 1
  print(f'Your final bill is: ${bill}')
elif size == 'M':
  bill = 20
  if add_pepperoni == 'Y':
    bill += 3
  if extra_cheese == 'Y':
    bill += 1
  print(f'Your final bill is: ${bill}')
else:
  bill = 25
  if add_pepperoni == 'Y':
    bill += 3
  if extra_cheese == 'Y':
    bill += 1
  print(f'Your final bill is: ${bill}')


# 3 - 5 love score

# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

lower_name1 = name1.lower()
lower_name2 = name2.lower()

true_score = lower_name1.count('t') + lower_name1.count('r') + lower_name1.count('u') + lower_name1.count('e') + lower_name2.count('t') + lower_name2.count('r') + lower_name2.count('u') + lower_name2.count('e')

love_score = lower_name1.count('l') + lower_name1.count('o') + lower_name1.count('v') + lower_name1.count('e') + lower_name2.count('l') + lower_name2.count('o') + lower_name2.count('v') + lower_name2.count('e')

string_score = str(true_score)+ str(love_score)

final_score = int(string_score)


if final_score < 10 or final_score > 90:
  print(f"Your score is {final_score}, you go together like coke and mentos.")
elif final_score >= 40 and final_score <= 50:
  print(f"Your score is {final_score}, you are alright together.")
else:
  print(f"Your score is {final_score}")


