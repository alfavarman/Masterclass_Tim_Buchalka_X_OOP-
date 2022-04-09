import datetime
import pytz


class Account:
    """Account class with balance"""

    @staticmethod
    def _current_time():
        utc_time = datetime.datetime.utcnow()
        return pytz.utc.localize(utc_time)

    def __init__(self, name, balance=0):
        self.name = name
        self.balance = balance
        self.transaction_list = []
        print(f"Account created for {self.name} with initial balance of {balance}")
        self.transaction_list.append((Account._current_time(), balance))

    def deposit(self, amount):
        if amount >= 0:
            self.balance += amount
            print(f'You deposited {amount}. Your Current Balance is: {self.balance}')
            self.transaction_list.append((Account._current_time(), amount))

    def withdraw(self, amount):
        if amount > self.balance:
            print(f'Withdraw request of: {amount} exceeds available balance ')
            self.show_balance()
            # self.transaction_list.append((pytz.utc.localize(datetime.datetime.utcnow())))
        elif amount >=0:
            self.balance -= amount
            print(f'You withdraw {amount}. Current Balance: {self.balance}')
            self.transaction_list.append((Account._current_time(), -amount))

    def show_balance(self):
        print(f'Your account balance is: {self.balance}')

    def show_transactions(self):
        for date, amount in self.transaction_list:
            if amount > 0:
                tran_type = 'deposit'
            else:
                tran_type = 'withdraw'
                amount *= -1
            print(f'{amount:6} {tran_type} on {date} local time {date.astimezone()}')


if __name__ == '__main__':
    Charles = Account('Charles', 0)
    # Charles.show_balance()

    Charles.deposit(1200)
    # Charles.show_balance()
    Charles.withdraw(123456)
    Charles.withdraw(12)
    # Charles.show_balance()
    Charles.show_transactions()
    print('#' * 60)

    Luq = Account('Luq', 800)
    Luq.deposit(350)
    Luq.withdraw(200)
    Luq.show_transactions()
