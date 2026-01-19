# rock,paper,scissor game
"""
import random

print("WELCOME TO ROCK,PAPER,SCISSOR GAME😊")
options = ('rock','paper','scissor')
player = None

while True:
    computer = random.choice(options)

    while player not in options:
        player = input('choose rock,paper or scissor ( q to quit ) ').lower()

        if player=='q':
            break
    if player=='q':
        break

    print(f'player:{player}')
    print(f'computer:{computer}')

    if player == computer:
        print('TIE!')
    elif player == 'rock' and computer == 'scissor':
        print('player won')
    elif player == 'scissor' and computer == 'paper':
        print('player won')
    elif player == 'paper' and computer == 'rock':
        print('player won')

    else:
        print('you lose,better luck next time')

    player = None

print('THANKS FOR PLAYING🙌')"""
