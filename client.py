"""
Class containing bank client operations.
"""

from account import Account

class Client(object):

    def __init__(self):
        self.accounts = set([])

    def open_account(self, account_type):
        # TODO: rename this variable
        a = Account(account_type)
        self.accounts.add(a)

    def close_account(self, account_number):
        if account_number in self.accounts:
            if self.accounts[account_number] == 0:
                del self.accounts[account_number]
            else:
                raise Exception("Account {} does not exist!".format(account_number))
        else:
            raise Exception("Account {} does not exist!".format(account_number))
