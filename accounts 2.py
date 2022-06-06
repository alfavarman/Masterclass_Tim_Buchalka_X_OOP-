import datetime
import time
import pytz


class Account:
    """Account is i"""

    @staticmethod
    def _current_time():                    # _ in front of name make it hidden
        utc_time = datetime.datetime.utcnow()
        return pytz.utc.localize(utc_time)

    def __init__(self, name, balance):
        self.name = name
        self.balance = balance
        self.transaction_list = []
        self.transaction_list.append((Account._current_time(), balance))
        print(f'Account Created For {self.name} with Initial Balance: {self.balance}')

    def deposit(self, amount):
        if 0 < amount:
            self.balance += amount
            print(f'{amount} Successfully deposited into {self.name} Account.')
            self.show_balance()
            self.transaction_list.append((Account._current_time(), amount))

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f'{amount} Successfully withdrawn from {self.name} Account.')
            self.show_balance()
            self.transaction_list.append((Account._current_time(), -amount))
        else:
            print(f'Invalid operation. Insufficient funds')

    def show_balance(self):
        print(f'Current Balance is: {self.balance}')

    def show_transactions(self):
        for date, amount in self.transaction_list:
            if amount > 0:
                transaction_type = 'deposited'
            else:
                transaction_type = 'withdrawn'
                amount *= -1
            print(f'{amount:6} {transaction_type} on {date} local time was {date.astimezone()}')


luq = Account('Luq', 200)
luq.deposit(300)
luq.show_balance()
luq.deposit(3000)
luq.show_balance()
luq.withdraw(4000)
luq.withdraw(2340)
luq.show_balance()
luq.show_transactions()
