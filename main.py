# project 1 - number guesser

import random

number = int(random.randint(1, 20))


for guesses in range(1, 7):
    guess = int(input('Please guess a number from 1 to 20 >>> '))
    if guess > number:
        print('wrong guess! Guess lower')
    elif guess < number:
        print('wrong guess! Guess higher')
    else:
        print('Correct Answer')
        break

if number == guess:
    print('Well Done!, it took you ' + str(guesses) + ' guesses!')
else:
    print('Wrong answer! The number wasa  ' + str(number))
