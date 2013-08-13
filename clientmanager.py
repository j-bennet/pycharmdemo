"""
Manages user account actions: login/logout
"""
from account import Account


class ClientManager(object):

    clients = {
        'jsmith' : {
            'pass': 'test',
            'logged_in': False,
            'accounts': {
                1111: Account(balance=50., type='checking'),
                2222: Account(balance=100., type='saving'),
            }
        },
        'mbrown': {
            'pass': 'test',
            'logged_in': False,
            'accounts': {
                3333: Account(balance=120., type='checking'),
            }
        },
    }

    def get_accounts(self, name):
        if name not in self.clients:
            raise Exception('Client {} does not exist!'.format(name))
        if not self.clients[name]['logged_in']:
            raise Exception('Client {} is not logged in!'.format(name))
        return self.clients[name]['accounts']

    def login(self, name, pwd):
        """
        Log this user in.
        Returns true if user is valid.
        """
        return name in self.clients and pwd == self.clients[name]['pass']

    def logout(self, name):
        """
        Log this user out.
        Returns true if user is valid.
        """
        if name in self.clients:
            self.clients[name]['logged_in'] = False
            return True
        return False