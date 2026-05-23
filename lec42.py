#BANKING PROGRAM

def show_balance(balance):
    print(f"Your bank balance is {balance:.2f}")

def deposit():
    dep=float(input("Enter the amount to be deposited :"))
    if dep>0:   
        return dep
    else:
        print("you must deposit positive value")
        return 0
    
def withdraw(balance):
    wit=float(input("Enter the amount you would like to withdraw :"))
    if wit>balance:
        print("Your withdrawal request exceeds your balance")
        return 0
    elif wit>0:
        return wit
    else:
        print("you must withdraw positive value")
        return 0

balance=0
is_running=True

while is_running:
    print("Welcoming to our banking program")
    print("1.Show balance")
    print("2.Deposit")
    print("3.Withdraw")
    print("4.Exit")

    choice=int(input("What would you like to do :"))
    if choice==1:
        show_balance(balance)
    elif choice==2:
        
        balance+=deposit()
    elif choice==3:
        
        balance-=withdraw(balance)
    elif choice==4:
        print("Thank you for visiting")
        is_running=False
    else:
        print("Invalid choice")