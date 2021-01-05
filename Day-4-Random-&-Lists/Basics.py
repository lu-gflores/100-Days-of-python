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

#Step 5

import random

#TODO-1: - Update the word list to use the 'word_list' from hangman_words.py
import hangman_words
chosen_word = random.choice(hangman_words.word_list)
word_length = len(chosen_word)

end_of_game = False
lives = 6

#TODO-3: - Import the logo from hangman_art.py and print it at the start of the game.
import hangman_art
print(hangman_art.logo)
#Testing code
# print(f'Pssst, the solution is {chosen_word}.')

#Create blanks
display = []
for _ in range(word_length):
    display += "_"

while not end_of_game:
    guess = input("Guess a letter: ").lower()

    #TODO-4: - If the user has entered a letter they've already guessed, print the letter and let them know.
    if guess in display:
      print("You've already guessed that letter.")
    #Check guessed letter
    for position in range(word_length):
        letter = chosen_word[position]
        # print(f"Current position: {position}\n Current letter: {letter}\n Guessed letter: {guess}")
        if letter == guess:
            display[position] = letter
    #Check if user is wrong.
    if guess not in chosen_word:
        #TODO-5: - If the letter is not in the chosen_word, print out the letter and let them know it's not in the word.
        print(f"'{guess}' is not in the word. You lose a life.'")
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("You lose.")

    #Join all the elements in the list and turn it into a String.
    print(f"{' '.join(display)}")

    #Check if user has got all letters.
    if "_" not in display:
        end_of_game = True
        print("You win.")

    #TODO-2: - Import the stages from hangman_art.py and make this error go away.
    import hangman_art
    print(hangman_art.stages[lives])