account_name = input("choose accont:\n")
 
print(f'You entered {account_name}')

class bankaccount:
    def __init__(self):
        self.balance = 10000
        print("debit & credit")

    def debit(self):
        amount = int(input("enter debit amount: "))
        self.balance += amount
        print("\n amount debit:",amount)

    def credit(self):
        amount = int(input("enter credit amount: "))
        if self.balance>=amount:
            self.balance-=amount
            print("\n credit:", amount)
        else:
            print("\n insufficient balance ")

    def display(self):
        print("\n available balance=",self.balance)

a = bankaccount( )
a.debit( )
a.credit( )
a.debit( )
a.display( )


print("saving account",a)
class bankaccount:
    def __init__(self):
        self.balance = 10000
        print("debit & credit")

    def debit(self):
        amount = int(input("enter debit amount: "))
        self.balance += amount
        print("\n amount debit:",amount)

    def credit(self):
        amount = int(input("enter credit amount: "))
        if self.balance>=amount:
            self.balance-=amount
            print("\n credit:", amount)
        else:
            print("\n insufficient balance ")

    def display(self):
        print("\n available balance=",self.balance)

a = bankaccount( )
a.debit( )
a.credit( )
a.display( )
