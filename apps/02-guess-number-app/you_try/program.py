import random

print('---------------------------------------------------------------------------------------------------------------')
print('                                             GUESS THE NUMBER GAME')
print('---------------------------------------------------------------------------------------------------------------')

the_number = random.randint(0,100)
guess = -1
guess_count = 0
name = input('Player, what is your name? ')

while guess != the_number:
    guess_text = input('Guess a number between 0 and 100: ')
    guess = int(guess_text)

    if guess < the_number:
        guess_count += 1
        print('{1}, your guess {0} is lower than the number, and you have made {2} guesses.'.format(guess,name,guess_count))
    elif guess > the_number:
        guess_count += 1
        print('{1}, your guess {0} is higher than the number, and you have made {2} guesses'.format(guess,name,guess_count))
    else:
        print('You won, taking {0} tries to guess the number!'.format(guess_count))
