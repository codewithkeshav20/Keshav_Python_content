
# 1. python first program
"""print("i really like pizza")
print("and burger")"""

# 2. variables
"""# strings
name = "keshav"
surname_is = "sharma"
#integer
age_is = 15
flat_no = 12
#float
cgpa = 6.99
total = 4.44
#boolean
is_available = True

print(f"the name is {name} and is {age_is} yr old with a cgpa "
      f"of {cgpa}")
if is_available:
    print("yes its true")
else:
    print("fake")"""

# 3. typecasting
"""name = 'bro'
age = 15
cgpa = 6.6
is_alive = True

name = bool(name)
print(name)
age = str(age)
print(type(age))
cgpa = int(cgpa)
print(cgpa)"""

# 4.user input
"""item = input("enter ur item")
price = float(input("enter the price"))
quantity = float(input("enter the quantity"))
total = price*quantity
print(f"u bought {item} and ur total is ${total}")"""

#5. madlibs project

#6. arithmatic math
"""x = 3
y = -4
z =4.44

#result = round(z)
#result = abs(y)
#result = pow(3,2)
#result = max(x,y,z)
print(result)"""

"""import math

x = 9.1
print(math.pi)
print(math.e)
print(math.sqrt(x))
print(math.ceil(x))
print(math.floor(x))"""

"""#find out the circumference 2*pie*r of circle
import math
radius = float(input("enter the radius"))
circumference = 2*math.pi*radius
print(f"the circumference is {round(circumference,5)}cm")
"""

"""# pie*r**r
area = math.pie * pow(r,2)
# sqrt a**2+b**2
area = math.sqrt(pow(a,2)+pow(b,2))"""

# 7. if statement
"""name = input("enter ur name")
if name =="":
    print("pls enter a name")
else:
    print(f" your name is {name}")"""

# 8. calculator program
# 9. weight conversion program
# 10. temperature conversion program

# 11.logical operators
"""temp = int(input("enter the temp"))
is_sunny = True

if temp>10 and is_sunny:
    print("its hot outside")
elif temp<10 and is_sunny:
    print("freezing")
else:
    print("invalid")"""

# 12.conditional expressions
"""passcode = 'keshav'
unlock = 'acess' if passcode=='keshav' else 'denied'
print(unlock)"""

"""a=10
b=-20
sum = 'positive' if a+b>0 else 'negative'
print(sum)"""

# 13. string methods
"""name ='keshavv'
phone = '892-223-231-444'
#result = name.find("v")
#result = name.rfind("v")
# result = name.capitalize()
# result = name.upper()
# result = name.isdigit()
# result = name.isalpha()
# result = phone.count("-")
# result = phone.replace("-","*")
print(result)"""

"""name = input("enter number")
if not name.find(" ")==-1:
    print("no spaces allowed")
else:
    print("retry")"""

# 14.string indexing
"""
num = "459-433-252-432"
#r = num[1:4]
#r = num[:5]
#r = num[::2]
r = num[-3:]
print(f"the last three digit is XXX-XX-XXX-{r}")"""

# 15.format specifier
"""
p1= 694.321
print(f"price is ${p1:+,.5f}")
print(f"price is ${p1:^99}")"""

# 16. while loop
"""
name = input("enter ur name")
while name=="":
    print("pls enter ur name")
    name = input("enter ur name")

print(f"hello {name}")"""

"""num = int(input("enter bw 1 to 10"))
while num<1 or num>10:
    print("number should be bw 1 to 10")
    num = int(input("enter bw 1 to 10"))

print(f"ur number is {num}")"""

# 17.compound interest calculator

# 18.for loops
"""
for x in reversed(range(0,11)):
    print(x)
print("happy new year")

for x in range(0,40):
    if x==23:
        continue
    else:
        print(x)"""

# 19. countdown timer program

# 20. nested loop
"""rows = int(input("enter the rows"))
columns = int(input("enter the columns"))
symbol = input("enter the symbols")
for x in range(rows):
    for y in range(columns):
        print(symbol,end=" ")
    print()"""

# 21. list, set and tuples
"""LIST[] ---> ordered and changeable"""
# fruits = ['mango','coconut','banana','lichi','lichi']
# print(fruits[::2])
"""for fruit in fruits:
    print(fruit,end=" ")"""
# print("orange" in  fruits)
# fruits[0]='orange'
# fruits.append('guava')
# fruits.remove('mango')
# fruits.insert(0,'watermelon')
# fruits.reverse()
# fruits.sort()
# print(fruits.index('lichi'))
# print(fruits.count('lichi'))

"""SET{}  ----> unordered and immutable"""
# fruits = {'mango','coconut','banana','lichi','lichi'}
# fruits.add('kiwi')
# fruits.pop()
#fruits.clear()

""" TUPLE() ------> ordered and unchangable"""
# fruits = ('mango','coconut','banana','lichi','lichi')
# print(fruits.count('lichi'))
# print(fruits.index('coconut'))

# 22. shopping cart program

# 23. 2D collection

"""fruits = ['mango','banana','orange']
sweets = ['barfi','ladoo','jalebi']

pairs = [fruits,sweets]"""

# print(pairs[0][2])

"""pairs = (['mango','banana','orange',
         'barfi','ladoo','jalebi'])
for pair in pairs:
    print(pair,end=" ")
print()"""

"""num_pad = ((1,2,3),
           (4,5,6),
           (7,8,9),
           ('*',0,'#'))
for row in num_pad:
    for num in row:
        print(num,end=" ")
    print()"""

# 24.quiz game

# 25.Dictionaries
"""
combinations = {'black':'chochlate',
                'berry':'pink'}"""

# print(combinations.get('black'))
# combinations.update({'purpule': 'grape'})
# combinations.update({'berry': 'grape'})
# combinations.pop('berry')
# combinations.popitem()

"""keys = combinations.keys()
print(keys)

for key in keys:
    print(key)"""

"""values = combinations.values()

for value in values:
    print(value)"""

"""items = combinations.items()

for item in items:
    print(item)"""

"""for key,value in combinations.items():
    print(f'{key}:{value}')"""

# 26. concession stand program

#27. random numbers
"""
import random

low = 1
high = 100
option = ['1','2']

# option = ('yes','no','maybe')
# number = random.randint(low,high)
# number = random.random()
# number = random.choice(option)
number = random.shuffle(option)
print(option)"""

# 28.number guessing game

# 29. rock,paper,scissor game

# 30. dice roller program #skipped for now

# 31. functions
"""def car(name,price):
    print(f'you want {name} and price is {price}cr')
    print(f'you dream car is {name}')
    print(f'but budget is not is {price}cr')

car('ferrari',45)
print()
car('prosche',80)
"""

"""
def name(first,last):
    first = first.capitalize()
    last = last.upper()
    return first + " " + last

full_name = name('keshav','sharma')
print(full_name)

also = name('sanaya','sharma')
print(also)"""

# 32.default arguments
"""
def net_price(list_price,discount=0,tax=0.5):
    return list_price*(1-discount)*(1+tax)

print(net_price(500))
print(net_price(500,0.1,03))"""

"""import time

def set_time(end,start=0):
    for x in range(start,end+1):
        print(x)
        time.sleep(1)
    print('done')

set_time(2)"""

# 33.keyword argument
"""
def welcome(greet,title,first,last):
    return(f'{greet} {title} {first} {last}')

welcome(greet='hi',first='mr',title='kishu',last='sharma')"""

# print('1','2','hi',sep='-')
"""
def phone(first_digit,last_digit):
    return(f'{first_digit}-{last_digit}')

print(phone('87650','93043'))
print(phone('8eff50','93we4'))"""

















