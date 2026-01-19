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
