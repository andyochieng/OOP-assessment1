
class BankAccount:
    def __init__(self, initial_balance=0):
        self.__balance = initial_balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Total deposited: Sh{amount}")
        else:
            print("Deposited amount can't be negative")

    def withdraw(self, amount):
        if amount > 0:
            if amount<=self.__balance:
                self.__balance -= amount
                print(f"Total withdrawal: Sh{amount}")
            else:
                print("insufficient funds")
        else:
            print("Withdrawal amount can't be negative")

    def get_balance(self):
        return self.__balance

account = BankAccount(5000)
account.deposit(300)
print("Your balance is:", account.get_balance())
account.withdraw(40)
print("Your balance is:", account.get_balance())
account.withdraw(40000)
print("Your balance is:", account.get_balance())
