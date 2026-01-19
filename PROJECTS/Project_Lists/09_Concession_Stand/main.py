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
