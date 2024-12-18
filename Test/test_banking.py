from banking import Transactions
from banking import Account
from datetime import datetime
now = datetime.now()
date = now.strftime("%Y-%m-%d")


def test_amount_no_date():
    my_test_amount = 100.0
    my_test_transaction = Transactions(my_test_amount)
    assert my_test_transaction.amount == my_test_amount
    assert my_test_transaction.time_stamp == date


def test_amount_date_passed():
    my_test_amount = 100.0
    my_test_date = '1999-01-01'
    my_test_transaction = Transactions(my_test_amount, my_test_date)
    assert my_test_transaction.amount == my_test_amount
    assert my_test_transaction.time_stamp == my_test_date


def test_account_deposit_is_pos():
    my_test_amount = -100.0
    my_test_amount_pos = my_test_amount * -1
    my_test_account = Account()
    my_test_account.deposit(my_test_amount)
    assert my_test_amount_pos == my_test_account.amount[0]


def test_account_deposits_appended():
    # my_test_dep_1 = 150.0
    # my_test_dep_2 = 230.0
    my_test_transaction_list = [150.0, 230.0]
    my_test_account = Account()
    my_test_account.deposit(my_test_transaction_list[0])
    my_test_account.deposit(my_test_transaction_list[1])
    assert repr(my_test_account.transactions) == repr(my_test_transaction_list)


def test_account_withdraw_is_neg():
    my_test_amount = 100.0
    my_test_amount_neg = my_test_amount * -1
    my_test_account = Account()
    my_test_account.withdraw(my_test_amount)
    assert my_test_amount_neg == my_test_account.amount[0]


def test_account_withdraw_appended():
    # my_test_dep_1 = 150.0
    # my_test_dep_2 = 230.0
    my_test_transaction_list = [-150.0, -230.0]
    my_test_account = Account()
    my_test_account.withdraw(my_test_transaction_list[0])
    my_test_account.withdraw(my_test_transaction_list[1])
    assert repr(my_test_account.transactions) == repr(my_test_transaction_list)


def test_account_get_balance_no_transactions_zero_ret():
    my_test_account = Account()
    my_test_account_balance = my_test_account.account_balance
    assert my_test_account_balance == 0


def test_account_get_balance_with_known_transactions():
    my_test_account_balance = 100 - 90 + 10
    my_test_account = Account()
    my_test_account.deposit(100)
    my_test_account.withdraw(90)
    my_test_account.deposit(10)
    my_test_account_transactions_balance = my_test_account.get_balance()
    assert my_test_account.account_balance == my_test_account_balance
