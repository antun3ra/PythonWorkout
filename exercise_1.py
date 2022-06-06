def guessing_game():
    from random import randint

    name = input(
        'Hello! Welcome to THE GUESSING GAME! Please insert your name: ')
    number = randint(0, 100)
    guess = int(
        input(f' Hey, {name}, try to guess the secret number between 0 and 100: '))

    while guess != number:
        if guess > number:
            guess = int(input(f'That\'s too high, {name}! Please try again: '))
        else:
            guess = int(input(f'That\'s too low, {name}! Please try again: '))

    if guess == number:
        print(
            f'CONGRATULATIONS {name}!!! That\'s absolutely right! Secret number was {number}! You did it!!')


guessing_game()
