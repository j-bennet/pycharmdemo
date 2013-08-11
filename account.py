"""
Defines user's bank account and implements basic actions on it.
"""
class Account(object):

    def __init__(self, userid):
        self.userid = userid
        self.balance = 0

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if self.balance <= amount:
            self.balance -= amount
        else:
            raise Exception("Insufficient funds!")