# slot machine
"""
import random

def spin_row():
    symbols=['🍒','🍉','🍋','🔔','⭐']
    return [random.choice(symbols) for _ in range(3)]

def print_row(row):
    print('*************')
    print(" | ".join(row))
    print('*************')


def get_payout(row,bet):
    if row[0]==row[1]==row[2]:
        if row[0]=='🍒':
            return bet*3
        elif row[0]=='🍉':
            return bet*4
        elif row[0]=='🍋':
            return bet*5
        elif row[0]=='🔔':
            return bet*10
        elif row[0]=='⭐':
            return bet*20
    return 0

def main():
    print('-------------------------')
    print('welcome to slot machine')
    print('symbols:🍒🍉🍋🔔⭐')
    print('-------------------------')

    balance = 100
    while balance>0:
        print(f"current balance is {balance}")

        bet = input("place ur bet")

        if not bet.isdigit():
            print('pls enter valid amount' )
            continue

        bet=int(bet)

        if bet>balance:
            print("insufficient funds")
            continue

        if bet<=0:
            print("bet should be more than 0")
            continue

        balance-=bet

        row=spin_row()
        # print(row)

        print_row(row)

        payout=get_payout(row,bet)
        if payout>0:
            print(f"you won ${payout} ")
        else:
            print("Better luck next time")

        balance +=payout

        play_again = input("play again? (y/n)")

        if play_again!='y':
            break

    print('-------------------------')
    print(f'game over , ur final balance is ${balance}')
    print('-------------------------')

if __name__=='__main__':
    main()"""
