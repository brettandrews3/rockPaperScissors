# Rock, paper, scissors, SMASH!

import random

print('Welcome to Rock, Paper, Scissors.\n')
random_choice = random.randint(0,2)

# Alternate randomizer:
"""
choices = ['rock', 'paper', 'scissors']
random_choice = random.choice(choices)
"""

# The computer makes its choice:
if random_choice == 0:
    random_choice = 'rock'
elif random_choice == 1:
    random_choice = 'paper'
else:
    random_choice = 'scissors'

# Next, the user makes their choice:
user_choice = input('What do you choose: rock, paper, or scissors?\n')

# Print the choices...
print('You chose', user_choice, 'and the computer chose', random_choice + '.')