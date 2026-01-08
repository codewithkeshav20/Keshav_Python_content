
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
    main()




