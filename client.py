"""
Class containing bank client operations.
"""

from account import Account


class Client(object):

    def __init__(self):
        """
        Create a new client.
        """
        self.accounts = {}

    def open_account(self, account_type):
        """
        Open a new account specifying the account type.
        """
        # TODO: rename this variable
        a = Account(account_type)
        self.accounts.add(a)

    def close_account(self, account_number):
        """
        Close account. Will throw an error if
        account does not exist, or still has funds.
        """
        if account_number in self.accounts:
            if self.accounts[account_number] == 0:
                del self.accounts[account_number]
            else:
                raise Exception("Account {} has non-zero funds!".format(account_number))
        else:
            raise Exception("Account {} does not exist!".format(account_number))

    def make_transfer(self, account_from, account_to, amount):
        """
        Transfer money from one account to another
        """
        if amount < 0:
            raise Exception("Negative amount: {}!".format(amount))
        if account_from not in self.accounts:
            raise Exception("'From' account # {} does not exist!".format(account_from))
        if account_to not in self.accounts:
            raise Exception("'To' account # {} does not exist!".format(account_to))

        src = self.accounts[account_from]
        dst = self.accounts[account_to]
        src.withdraw(amount)
        dst.deposit(amount)

    def print_accounts(self):
        """
        Print out client accounts information:
        Account # 111 (checking): 1000.00
        Account # 222 (saving): 2000.00
        """
        for account_number in self.accounts:
            print "Account # {} ({}): {}".format(
                account_number,
                self.accounts[account_number].type,
                self.accounts[account_number].balance)
