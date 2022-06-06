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
        self.__name = name
        self.__balance = balance
        self.transaction_list = [(Account._current_time(), balance)]
        print(f'Account Created For {self.__name} with Initial Balance: {self.__balance}')

    def deposit(self, amount):
        if 0 < amount:
            self.__balance += amount
            print(f'{amount} Successfully deposited into {self.__name} Account.')
            self.show_balance()
            self.transaction_list.append((Account._current_time(), amount))

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            print(f'{amount} Successfully withdrawn from {self.__name} Account.')
            self.show_balance()
            self.transaction_list.append((Account._current_time(), -amount))
        else:
            print(f'You failed to withdrawn {amount}. Insufficient funds on your account.')
            self.show_balance()

    def show_balance(self):
        print(f'Current Balance is: {self.__balance}')

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
print('code: luq.balance = 0.1 #hacker attack')
luq.__balance = 0.1
luq.withdraw(4000)
luq.withdraw(2340)

luq.show_transactions()
