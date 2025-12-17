import pytest
from make_account import make_account

def test_basic_account():
    deposit, withdraw = make_account(100)
    assert deposit(50) == 150
    assert withdraw(30) == 120

def test_overdraw():
    deposit, withdraw = make_account(50)
    with pytest.raises(ValueError):
        withdraw(100)

def test_balance_persists():
    deposit, withdraw = make_account(100)
    deposit(10)
    deposit(20)
    assert withdraw(30) == 100

