
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

# 34. *args and **kwargs

# *args  [ allow multiple non keyword arguments ]
"""
def add(*nums):
    total = 0
    for num in nums:
        total+=num
    return(total)

print(add(1,2,3))"""

# **kwargs [ allow multiple keyword arguments]
"""
def address(**kwargs):
    for key,value in kwargs.items():
        print(f'{key} : {value}')

address(state='up',city='ghz',flat=33)"""
"""
def shipping_label(*args,**kwargs):
    print('---------SHIPPPING ADDRESS--------')
    for arg in args:
        print(arg,end=" ")
    print()
    print(f'{kwargs.get('state')},{kwargs.get('city')}')
    print(f'{kwargs.get('flat')},{kwargs.get('tower')}')

shipping_label('Mr','Keshav','Sharma', state='Uttar Pradesh',city='Merut',flat='33',tower='Fierce Tower')
print('----------------------------------')"""

# 35.iterables
"""
number= 1,2,3,4,5,6

for num in number: # here 'number' is iterable where loop iterate over and over.
    print(num,end=' ')"""

# 36. membership  operator (in,not in)
"""
name = 'keshav','yash','raj'

if 'keshav' not in name:
    print('false')
elif 'keshav' in name :
    print('true')
else:
    print('not found')"""

# 37. list comprehensions
"""
double = [x*2 for x in range(1,11)]
print(double)"""

"""fruits=['mango','banana','strawberry']
fruits_list = [fruit[0] for fruit in fruits]
print(fruits_list)"""

"""numbers = 1,-1,2,3,-4

one=[num for num in numbers if num>1]
print(one)

evens=[num for num in numbers if num%2==0 ]
print(evens)"""

# 38. match-case statements
"""def day_of_week(day):
    match day:
        case 1:
            return ("sunday")
        case 2:
            return ("monday")
        case 3:
            return ("tuesday")
        case _:
            return ("soon")

print(day_of_week(4))"""


"""def is_weekend(day):
    match day:
        case "sunday"|"saturday":
            return (True)
        case "monday"|"tuesday"|"wednesday"|"thursday"|"friday":
            return(False)
        case _:
            return ("invalid day")

print(is_weekend('saturday'))"""

# 39.modules (import module)
#this is example file
"""pi=3.14

def square(x):
    return(x**2)

def circumference(r):
    return (2*pi*r)

def add(a,b):
    return (a+b)"""

"""import example

# result=example.pi
# result=example.square(3)
# result=example.circumference(2)
# result=example.add(3,4)
print(result)"""

# 40.scope resolution (LEGB) LOCAL,ENCLOSED,GLOBAL,BUILT-IN
"""
def fun1():
    x=1
    print(x)
def fun2():
    x = 2
    print(x)

fun1()
fun2()"""

# 41. if name=='main
"""
#script 1
def fav_food(food):
    print(f'ur favourite food is {food}')

def main():
    print('this is script 1')
    fav_food('pizza')
    print('goodbye')

if __name__=='__main__':
    main()


#script2
from script1 import*

def fav_drink(drink):
    print(f'my favourite drink is {drink}')

def main():
    print('this is script 2')
    fav_drink('cold coffee')
    fav_food('burger')
    print('goodbye')

if __name__=='__main__':
    main()"""

# 42.banking program

# 43.slot machine

# 44.encryption program

# 45. hangman game (skipped for now)

# 46. python object oriented programming
"""
from car import car

car1=car('mustang','3cr','2022','11')
print(car1.name)
print(car1.price)
print(car1.year)
print(car1.mileage)


car1.drive()
car1.stop()"""

# 47. class variables
"""
class student:

    class_year = 2020
    num_student = 0

    def __init__(self,name,roll,):
        self.name=name
        self.roll=roll
        student.num_student+=1

student1=student('yash','324')
student2=student('harsh','154')
student2=student('posh','994')


print(student1.name)
print(student2.roll)
print(student1.class_year)
print(student2.class_year)
print(student.class_year)

print(student.num_student)"""

# 48.inheritance
"""
class animal:
    def __init__(self,name,breed):
        self.name=name
        self.breed=breed
        self.is_alive = True

    def living(self):
        print(f'the {self.name} is alive yes it is {self.is_alive}')

class dog(animal):
    def bite(self):
        print(f'{self.name} bite me ')

class cat(animal):

    def speak(self):
        print('meow')

dog1=dog('rocky','golden retriever')
cat1=cat('perry','persian')

print(cat1.breed)
print(dog1.name)
print(dog1.is_alive)
cat1.living()
dog1.living()
cat1.speak()
dog1.bite()"""

# 49.multiple inheritance
"""
class animal:

    def __init__(self,name):
        self.name=name

    def eat(self):
        print(f'{self.name} always eat')

class prey(animal):
    def flee(self):
        print(f'{self.name} is fleeing')

class predator(animal):
    def hunt(self):
        print(f'{self.name}  is hunting')

class rabbit(prey):
    pass

class eagle(predator):
    pass

class fish(prey,predator):
    pass

rabbit1 = rabbit("bunny")
rabbit1.flee()

eagle1=eagle("hawkey")
eagle1.hunt()

fish1=fish("nemo")
fish1.flee()
fish1.hunt()

fish1.eat()
eagle1.eat()"""

# 50.super()
"""
class shape:
    def __init__(self,color,filled):
        self.color=color
        self.filled=filled

    def describe(self):
        print(f"it is {self.color} and {'filled' if self.filled else 'not filled'}")

class circle(shape):
    def __init__(self,color,filled,radius):
        super().__init__(color,filled)
        self.radius=radius

    def describe(self):
        print(f'it is round in shape')
        super().describe()

class square(shape):
    def __init__(self,color,filled,width):
        super().__init__(color,filled)
        self.width=width

circle1=circle('red',True,4)
# square1=square('yellow',False,2.2)
# print(circle1.color)
# print(square1.width)

circle1.describe()"""

# 51.Polymorphism
"""
from abc import ABC,abstractmethod

class shape:

    @abstractmethod
    def area(self):
        pass

class circle(shape):
    def __init__(self,radius):
        self.radius=radius

    def area(self):
        return 3.14*self.radius**2

class square(shape):
    def __init__(self,side):
        self.side=side

    def area(self):
        return self.side**2

class pizza(circle):
    def __init__(self,topping,radius):
        super().__init__(radius)
        self.topping=topping


shapes=[circle(4),square(5),pizza('pepperoni',11)]

for shape in shapes:
    print(f'{shape.area()}cm ')"""

# 52.duck typing
"""
class Animal:
    def __init__(self,name):
        self.name = name

    alive = True

class dog(Animal):

    def speak(self):
        print(f'{self.name} : woof')

class cat(Animal):

    def speak(self):
        print(f'{self.name} : meow')

class car:
    alive = False
    def speak(self):
        print('honk')

animals=[dog('buro'),cat('tom'),car()]

for animal in animals:
    animal.speak()
    print(animal.alive)"""

# 53.static methods
"""
class Employee:

    def __init__(self,name,position):
        self.name=name
        self.position=position

    def get_info(self):
        return(f'{self.name}={self.position}')

    @staticmethod
    def is_valid_position(position):
        positions=['manager','cook','ceo']
        return position in positions

print(Employee.is_valid_position('manager'))
print(Employee.is_valid_position('customer'))

employee1=Employee('raj','manager')
employee2=Employee('tanishq','scientist')

print(employee1.get_info())
print(employee2.get_info())"""

# 54.class methods
"""
class Student:

    count=0
    total_gpa=0

    def __init__(self,name,gpa):
        self.name=name
        self.gpa=gpa
        Student.count+=1
        Student.total_gpa+=gpa
    #instance method
    def get_info(self):
        return(f'{self.name} : {self.gpa}')

    @classmethod
    def get_count(cls):
        return (f'toal number of students : {cls.count}')

    @classmethod
    def average(cls):
        if cls.count==0:
            return 0
        else:
            return(f'total avergage : {cls.total_gpa/cls.count}')

student1=Student('yash',2.4)
student2=Student('taj',3.3)
student3=Student('shyam',1.0)

print(student1.get_info())
print(student2.get_info())
print(student3.get_info())
print(Student.get_count())
print(Student.average())"""

# 55.Magic methods
"""
class Book:

    def __init__(self,title,author,num_pages):
        self.title=title
        self.author=author
        self.num_pages=num_pages

    def __str__(self):
        return f"{self.title} by {self.author}"

    def __eq__(self,other):
        return self.title == other.title and self.author==other.author

    def __lt__(self,other):
        return self.num_pages<other.num_pages

    def __gt__(self,other):
        return self.num_pages>other.num_pages

    def __add__(self,other):
        return f"{self.num_pages + other.num_pages} pages"

    def __contains__(self,keyword):
        return keyword in self.title or keyword in self.author

    def __getitem__(self,key):
        if key == "title":
            return self.title
        elif key == "author":
            return self.author
        elif key == "num_pages":
            return self.num_pages
        else:
            return f"{key} not found"

book1=Book('hobbit','jrr',310)
book2=Book('harry potter','jk',223)
book3=Book('lion','lewis',172)
book4=Book('lion','lewis',172)

print(book1)
print(book3==book4)
print(book3<book1)
print(book3>book1)
print(book1+book2)
print('lion' in book1)
print('jrr' in book1)

print(book2["title"])
print(book4["author"])
print(book1["num_pages"])
print(book2["audio"])"""

# 56.property
"""
class Rectangle:

    def __init__(self,width,height):
        self._width=width
        self._height=height

    @property
    def width(self):
        return f"width : {self._width:.2f}cm"

    @property
    def height(self):
        return f"height : {self._height:.2f}cm"

    @width.setter
    def width(self,new_width):
        if new_width>0:
            self._width = new_width
        else:
            print('width should be greater than 0')

    @height.setter
    def height(self, new_height):
        if new_height > 0:
            self._height = new_height
        else:
            print('height should be greater than 0')

    @width.deleter
    def width(self):
        del self._width
        print("width is now deleted")

    @height.deleter
    def height(self):
        del self._height
        print("height is now deleted")

rectangle = Rectangle(3.11,5.31)

rectangle.width=44
rectangle.height=-1
print(rectangle.width)
# print(rectangle.height)

del rectangle.width"""

# 57.decorators
"""
def jacket(func):
    def wait(*args,**kwargs):
        print("you added a black leather jacket")
        func(*args,**kwargs)
    return wait

@jacket
def outfit(feature):
    print(f"here is your {feature} outfit")

outfit("complete")"""

# 58.exception handling
"""
try:
    number=int(input("enter the numbers "))
    print(1/number)

except ZeroDivisionError:
    print("cant divide by 0 ")

except ValueError:
    print("pls enter only numbers ")

except Exception:
    print("something went wrong")

finally :
    print("Correct your input")"""

# 59. File Detection
"""
import os

# file_path="..//python notes extra//test.txt"
file_path="C:\\Users\\kishu\\OneDrive\\Desktop\\test.txt"


if os.path.exists(file_path):
    print(f"the location {file_path} exists")

    if os.path.isfile(file_path):
        print("this is a file")
    elif os.path.isdir(file_path):
        print("this is a directory")
else:
    print("the location doesnt exist")"""

# 60.writing files
#xyz.txt
"""employees = ["keshav","yash","rahul","sanya"]

file_path = "..//python notes extra//test.txt"
file_path="C:\\Users\\kishu\\OneDrive\\Desktop\\test.txt"
try:
    with open(file_path, "w") as file:
        for employee in employees:
            file.write(employee + " ")
        print(f"txt file {file_path} was created")
except FileExistsError:
    print("the file already exists")"""

#xyz.json
"""import json
employees = {"keshav":"manager",
             "slary":300000,
             "rahul":"client",
             "time":33}

file_path = "..//python notes extra//test.json"
file_path="C:\\Users\\kishu\\OneDrive\\Desktop\\test.json"
try:
    with open(file_path, "w") as file:
        json.dump(employees,file,indent=4)
        print(f"json file {file_path} was created")
except FileExistsError:
    print("the file already exists")"""

#xyz.csv
"""import csv
import json
employees = [["keshav","manager"],
             ["slary",300000],
             ["rahul","client"],
             ["time",33]]

file_path = "..//python notes extra//test.csv"
file_path="C:\\Users\\kishu\\OneDrive\\Desktop\\test.csv"
try:
    with open(file_path, "w") as file:
        writer=csv.writer(file)
        for row in employees:
            writer.writerow(row)
        print(f"csv file {file_path} was created")
except FileExistsError:
    print("the file already exists")"""

# 61.reading files
"""#import json
#import csv

file_path="C:\\Users\\kishu\\OneDrive\\Desktop\\test.txt"
# file_path="C:\\Users\\kishu\\OneDrive\\Desktop\\test.json"
# file_path="C:\\Users\\kishu\\OneDrive\\Desktop\\test.csv"

try:
    with open(file_path,"r") as file:
        content=file.read()
        # content=json.load(file)
        # content=csv.reader(file)
        #for line in content:
        #             print(line)
        print(content)
except FileNotFoundError:
    print("file not found")
except PermissionError:
    print("you do not have permission to read the file")
"""

# 62.dates and times

# import datetime

"""date=datetime.date(2026,2,11)
today=datetime.date.today()
print(today)"""

"""time=datetime.time(11,50,22)
now=datetime.datetime.now()

now=now.strftime("time : %H:%M:%S and date: %y-%m-%d")
print(now)"""

"""target_datetime=datetime.datetime(2020,1,29,12,33,59)
current_datetime=datetime.datetime.now()

if target_datetime<current_datetime:
    print("time passed")
else:
    print("time not passed")"""

# 63.alarm clock

print('---------THE END😍😊------------')

















