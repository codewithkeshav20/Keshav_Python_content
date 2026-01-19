# number guessing game
"""
import random

print('WELCOME TO PYTHON GUESSING GAME 😍')

low = 1
high = 100
guesses = 0
answer = random.randint(low, high)
is_running = True

while is_running:
    guess = input('Guess a number between 1 and 100: ').strip()

    if not guess.isdigit():
        print("Please enter a valid number")
        continue

    guess = int(guess)
    guesses += 1

    if guess < low or guess > high:
        print("❌ Out of range! Try between 1 and 100")

    elif guess < answer:
        print("📉 Too low! Try again")

    elif guess > answer:
        print("📈 Too high! Try again")

    else:
        print("🎉 CORRECT! You guessed it!")
        print(f"The answer was: {answer}")
        print(f"Number of guesses: {guesses}")
        is_running = False"""
