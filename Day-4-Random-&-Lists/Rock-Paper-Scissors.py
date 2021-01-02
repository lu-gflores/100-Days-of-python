rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
import random
# place strings in a list
game = [rock, paper, scissors]

user_choice = int(input('What do you choose? Type 0 for Rock, 1 for Paper, or 2 for Scissors '))

if user_choice > 3 or user_choice < 0:
  print('Invalid number, try again!')
else:  
  # length of the game list
  length_game = len(game)
  random_choice = random.randint(0, length_game - 1)
  # for displaying computer choice string
  computer_choice = game[random_choice]

  ##prints player choices
  print(game[user_choice])
  print(f'Computer chose: {computer_choice}')

  if user_choice == random_choice:
    print('Draw')
  elif user_choice == 0 and random_choice == 1:
    print('You lose...')
  elif user_choice == 1 and random_choice == 2:
    print('You lose...')
  elif user_choice == 2 and random_choice == 0:
    print('You lose...')
  else:
    print('You win!') 