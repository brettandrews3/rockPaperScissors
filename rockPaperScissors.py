# Rock, paper, scissors, SMASH!

import random

# This variable will hold the winner info later in the code.
winner = ''

print('Welcome to Rock, Paper, Scissors.\n')
computer_choice = random.randint(0,2) # Keeps the computer to just 3 choices

# Alternate randomizer:
"""
choices = ['rock', 'paper', 'scissors']
computer_choice = random.choice(choices)
"""

# The computer makes its choice:
if computer_choice == 0:
    computer_choice = 'rock'
elif computer_choice == 1:
    computer_choice = 'paper'
else:
    computer_choice = 'scissors'

# Next, the user makes their choice:
user_choice = input('What do you choose: rock, paper, or scissors?\n')

# Print the choices...
print('You chose', user_choice, 'and the computer chose', computer_choice + '.\n')

if user_choice == computer_choice:
    winner = 'Tie'
