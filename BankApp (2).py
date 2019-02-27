import sys
class Bank:
    '''Customer Bank'''
    bankname="RomeoBank"
    
    def __init__(self,name,balance=0.0):
        self.name=name
        self.balance=balance
    def deposit(self,damt):
        self.balance=self.balance+damt
        print("Balance after deposit: ",self.balance)
    def withdraw(self,wamt):
        if wamt>self.balance:
            print("You have not sufficient balance!!!! please try again")
            sys.exit()
        self.balance=self.balance-wamt
        print("Balance after withdraw: ",self.balance)
print("Customer bank name: ",Bank.bankname)
name=input("Enter Name: ")
b=Bank(name)
while True:
    print("d-Deposit \nw-Withdraw \ne-exit")
    option=input("Enter your option")
    if option =='d' or option =='D':
        damt=float(input("enter amount: "))
        b.deposit(damt)
    elif option == 'w' or option == 'W':
        wamt=float(input("Enter amount: "))
        b.withdraw(wamt)
    elif option == 'e' or option =='E':
        print("Thanks for Banking")
        sys.exit()
    else:
        print("invalid option!!!!! please choose proper option")
