import random

print('I am thinking of a number between 1 and 20.')
randomNumber = random.randint(1,21)
counter = 0

while True:
    print('Take a guess.')
    guess = int(input())
    counter = counter + 1
    if guess < randomNumber:
        print('Your guess is too low.')
    elif guess > randomNumber:
        print('Your guess is too high.')
    else:
        break

print('Good job! You guessed my number in ' + str(counter) + ' guesses!')