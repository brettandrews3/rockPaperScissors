# Rock, paper, scissors, SMASH!

import random

print('Welcome to Rock, Paper, Scissors.')
random_choice = random.randint(0,2)

if random_choice == 0:
    random_choice = 'Rock'
elif random_choice == 1:
    random_choice = 'Paper'
elif random_choice == 2:
    random_choice = 'Scissors'

print('The computer chooses ', random_choice)