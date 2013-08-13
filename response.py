"""
Fake response class.
"""


class Response(object):

    PG_LOGIN = 'login'
    PG_THANKS = 'tnxbye'
    PG_CLIENT = 'client'
    PG_ACCOUNT = 'account'

    def __init__(self, page=None, data=None):
        self.page = page
        self.data = data

    @classmethod
    def create_login(self):
        return Response(self.PG_LOGIN)

    @classmethod
    def create_logout(self):
        return Response(self.PG_THANKS)

    @classmethod
    def create_account(self, data=None):
        return Response(self.PG_ACCOUNT, data=data)

    @classmethod
    def create_client(self, data=None):
        return Response(self.PG_CLIENT, data=data)