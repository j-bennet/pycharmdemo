"""
Defines user's bank account and implements basic actions on it.
"""


class Account(object):

    def __init__(self, balance=0, type="checking"):
        self.type = type
        self.balance = balance

    def deposit(self, amount):
        # TODO: check for negative amount
        self.balance += amount

    def withdraw(self, amount):
        if self.balance <= amount:
            self.balance -= amount
        else:
            raise Exception("Insufficient funds!")