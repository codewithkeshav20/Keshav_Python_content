# madlibs game
"""
adjective = input("enter descripption")
adjective2 = input("enter descripption")
noun = input("enter name,place or thing")
verb = input("ending with 'ing' ")

print(f"today i went to {adjective} place,"
      f"where i saw {noun} also it was"
      f"{adjective2} and i was {verb}")"""

# calculator program
"""
operator = input("enter a operator (+,-,/,*)")
num1 = float(input("enter first number"))
num2 = float(input("enter second number"))

if operator=='-':
    result = num1-num2
    print(round(result,2))
elif operator=='+':
    result = num1 + num2
    print(round(result, 2))
else:
    print("wrong operator ")"""

# weight conversion program
"""weight = int(input("enter your weight "))
unit = input("kg,lbs")
if unit=='kg':
    weight = weight*2.205
    print(f"your weight in lbs is {weight}" )
elif unit=='lbs':
    weight = weight/2.205
    print(f"your weight in kg is {weight}" )
else:
    print("enter correct unit")"""

# temperature conversion program
"""
temp = int(input("enter the temp"))
unit = input('c,f')

if unit=='c':
    temp = 9*temp/5+32
    print(f'temp in farenheight is {temp}')
elif unit =='f':
    temp =temp-32*5/9
    print(f'temp in celcius is {temp}')
else:
    print("invalid")"""

# compound interest calculator
"""
principle = 0
rate = 0
time = 0

while True:
    principle = float(input("enter the principle amount "))
    if principle<0:
        print("cant be less than 0")
    else:
        break

while True:
    rate = float(input("enter the rate amount "))
    if rate<0:
        print("cant be less than 0")
    else:
        break

while True:
    time = float(input("enter the time"))
    if time<0:
        print("cant be less than 0")
    else:
        break

total = principle*pow((1+rate/100),time)
print(f"balance after {time} yrs is ${total:.5f}")"""

# countdown timer program
"""
import time
timer = int(input("enter the duration in seconds "))
for x in range(timer,0,-1):
    seconds = x%60
    minutes = int(x/60)%60
    hours = int(x/3600)
    print(f"{hours:02}:{minutes:02}:{seconds:02}")
    time.sleep(1)

print("TIME'S UP! ")"""

# shopping cart program
"""
foods=[]
prices=[]
cart=[]
total = 0
print("welcome to shopping cart 😊")

while True:
    food = input ("enter the food u want ('q' to quit) ")
    if food.lower()=='q':
        break
    else:
        price = float(input("enter the price of food $"))
        foods.append(food)
        prices.append(price)

print("--------------YOUR CART 🛒----------------")
for food in foods:
    print(food)
for price in prices:
    total+=price
print("--------------YOUR TOTAL 💵----------------")

print(f"{total}$")"""

# quiz game
"""
questions = ('what is the largest number here ',
             'what is the smallest number here')
options = (('a.10','b.20','c.30','d.40'),
           ('a.3','b.2','c.33','d.1'))

answers =('d','d')

guesses=[]
score=0
question_num = 0

for question in questions:
    print('------------------------')
    print(question,end=" ")
    print()
    for option in options[question_num]:
        print(option)

    guess = input("enter ur answer ('a','b','c','d') ").lower()
    guesses.append(guess)
    if guess == answers[question_num]:
        score += 1
        print('correct')
    else:
        print('incorrect')
        print(f'{answers[question_num]} is the correct answer')

    question_num+=1

print('-------------------------------')
print('            RESULT             ')
print('-------------------------------')

print('answer:',end=" ")
for answer in answers:
    print(answer,end=" ")
print()

print('guess:',end=" ")
for guess in guesses:
    print(guess,end=" ")
print()

score=int(score/len(questions)*100)
print(f'ur score is {score}%')"""

# concession stand program
"""menu = {'nachos':3.3,
        'burger':3.2,
        'fries':2.1}

cart = []
total = 0

print('-------------MENU--------------')
for key,value in menu.items():
    print(f"{key:10}:${value:.2f}")

while True:
    food = input("select an item (q to quit)").lower()
    if food=='q':
        break
    elif menu.get(food) is not None:
        cart.append(food)

print('------------YOUR ITEMS----------')
for food in cart:
    total+=menu.get(food)
    print(food,end=" ")
print()
print('--------------------------------')
print(f'Your total is ${total}')"""

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

#





























