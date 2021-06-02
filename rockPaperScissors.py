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

# This if statement catches any incorrect inputs from the user:
if (user_choice != 'rock' and
        user_choice != 'paper' and
        user_choice != 'scissors'):
    user_choice = input('What do you choose: rock, paper, or scissors?\n')
print('Player chose ' + user_choice + '.\n')

# Print the choices...
# print('You chose', user_choice, 'and the computer chose', computer_choice + '.\n')

# Here's the winning conditions. If computer doesn't win and there's no tie, the Player wins.
if computer_choice == user_choice:
    winner = 'Tie'
elif computer_choice == 'rock' and user_choice == 'scissors':
    winner = 'Computer'
elif computer_choice == 'paper' and user_choice == 'rock':
    winner = 'Computer'
elif computer_choice == 'scissors' and user_choice == 'paper':
    winner = 'Computer'
else:
    winner = 'Player'

# The winner statement is driven by the elif statements above, filling in both players' answers:
if winner == 'Tie':
    print('We both chose ', computer_choice + '. It\'s a Tie! Let\'s play again.')
elif winner == 'Computer':
    print('I chose ' + computer_choice + ', and you chose ' + user_choice + '. Computer wins!')
elif winner == 'Player':
    print('I chose ' + computer_choice + ', and you chose ' + user_choice + '. Player wins!')
else:
    print('Hmm. No one won that round. Let\'s try again.')

# Super minor edit to trigger a git commit and push