from dataclasses import dataclass, field
from datetime import datetime
now = datetime.now()
date = now.strftime("%Y-%m-%d")


class Transactions:

    def __init__(self, amount: float, time_stamp: str = None):
        if time_stamp is not None:
            self.amount = amount
            self.time_stamp = time_stamp
        else:
            self.amount = amount
            time_stamp = date
            self.time_stamp = time_stamp

    def __str__(self):
        return self.get_transaction()

    def __repr__(self):
        return f'{self.amount}'

    def get_transaction(self):
        if self.amount > 0:
            return f'{self.time_stamp}: +${self.amount}'
        if self.amount < 0:
            amount = self.amount * -1
            return f'{self.time_stamp}: -${amount}'


@dataclass
class Account:
    account_balance: float
    transactions: list = field(default_factory=list)
    amount: list = field(default_factory=list)

    def __init__(self):
        self.account_balance = 0.0
        self.transactions = []
        self.amount = []

    def deposit(self, amount):
        if amount < 0:
            new_amount = amount * -1
        else:
            new_amount = amount

        transaction_instance = Transactions(new_amount)

        self.transactions.append(transaction_instance)
        self.amount.append(new_amount)

    def withdraw(self, amount):
        new_amount: float

        if amount > 0:
            new_amount = amount * -1
        else:
            new_amount = amount

        transaction_instance = Transactions(new_amount)

        self.transactions.append(transaction_instance)
        self.amount.append(new_amount)

    def get_balance(self):
        self.account_balance = sum(self.amount)

        print(self.account_balance)
