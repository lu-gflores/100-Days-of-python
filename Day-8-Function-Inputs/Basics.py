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