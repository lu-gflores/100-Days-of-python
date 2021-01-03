fruits = ['apple', 'peach', 'pear']

#for loop
# loops through a list within the for indentation
for fruit in fruits:
  print(fruit)
  print(fruit + ' pie')

# will print once since it is outside the for loop
print(fruits)

#Range function
#from one to ten, does not include 11
for number in range(1, 11, 3):
  print(number)

total = 0 

for number in range(1, 101):
  total += number
print(total)

# Exercises

# 5 - 1
# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆

#Write your code below this row 👇

total =  0
length = 0
average_height = 0
for height in student_heights:
  total += height
  length += 1 
  average_height = round(total / length )
print(average_height)


# 5 - 2 Exercise Find the higest test score

student_scores = input("Input a list of student scores ").split()
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])
print(student_scores)
# 🚨 Don't change the code above 👆

#Write your code below this row 👇

high_score = 0
for score in student_scores:
  if score > high_score:
    high_score = score
print(f'Highest score is: {high_score}')

# 5 - 3 Printing Even Numbers
total = 0
for number in range(2, 101, 2):
  total += number
print(total)


# 5- 4 Fizz Buzz
for number in range(1, 101):
  if number % 15 == 0:
    print('FizzBuzz')
  elif number % 5 == 0:
    print('Buzz')
  elif number % 3 == 0:
    print('Fizz')
  else:
    print(number)
