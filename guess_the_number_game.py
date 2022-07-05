import random

def guess(x):
    random_number = random.randint(1, x)
    guess = 0
    while guess != random_number:
        guess = int(input(f'Guess the number is between 1 and {x}: '))
        if guess < random_number:
            print('Guess again. Too low.')
        elif guess > random_number:
            print('Guess again. Too high.')

    print(f'Congratulations. You have guessed the number {random_number} correctly!!')
