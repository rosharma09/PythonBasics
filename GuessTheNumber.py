# This is a game to guess a number between a given range in 6 tries 

import random

print('Please enter your name:')
name = input()

print('Welcome '+name)

print('Well, '+name+ ' I am thinking of a number between 1 and 20')
randomNumber = random.randint(1,20) # generate a random number between 1 and 20

print('DEBUG : The number is '+str(randomNumber))

# Ask user to take a guess 

for guessTaken in range(1,7):
    print('Take a guess.')
    guess = int(input())

    if guess < randomNumber:
        print('Your Guess is too low.')
    elif guess > randomNumber:
        print('Your Guess is too high ')
    else:
        break # in case the guess and random number is correct

if guess == randomNumber:
    print('Great Job ' +name+ ' You have guessed the number in '+str(guessTaken)+ ' guesses' )
else:
    print('Nope ! The number i was thinking about was '+str(randomNumber))

