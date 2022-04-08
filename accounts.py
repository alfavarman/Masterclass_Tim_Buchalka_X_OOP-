class Account:
    """Account class with balance"""

    def __init__(self, name, balance):
        self.name = name
        self.balance = balance
        print(f"account created for {self.name}")

    def deposit(self, amount):
        if amount >= 0:
            self.balance += amount

    def withdraw(self, amount):
        if amount >= 0:
            self.balance -= amount

    def show_balance(self):
        print(f'Your account balance is: {self.balance}')


if __name__ == '__main__':
    Charles = Account('Charles', 0)
    Charles.show_balance()

    Charles.deposit(1.200)
    Charles.show_balance()
    Charles.withdraw(123)
    Charles.show_balance()