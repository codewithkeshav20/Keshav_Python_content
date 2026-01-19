# banking program
"""
def deposit(balance):
    amount=int(input("enter the amount to be deposited "))
    if amount<0:
        print("invalid amount")
        return 0
    else:
        return amount
def withdraw(balance):
    amount = int(input("enter the amount to be withdrawn "))
    if amount < 0:
        print("invalid amount")
        return 0
    elif amount>balance:
        print("insufficient amount")
        return 0
    else:
        return amount
def show_balance(balance):
    print(f"your balance is {balance}$")

def main():
    balance = 0
    is_running = True
    while is_running:
        print('------------------')
        print("BANKING PROGRAM")
        print('------------------')

        print("1.show balance")
        print("2.deposit")
        print("3.withdraw")
        print("4.exit")

        choice = input("enter your choice (1-4)")

        if choice == '1':
            show_balance(balance)
        elif choice == '2':
            balance += deposit(balance)
        elif choice == '3':
            balance -= withdraw(balance)
        elif choice == '4':
            print("THANK YOU FOR VISITING😊")
            is_running = False
        else:
            print("INVALID CHOICE")

if __name__=='__main__':
    main()"""
