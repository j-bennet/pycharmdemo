"""
This is the class we're going to use for our refactoring example.
It contains spaghetti code to clean up.
"""
from client import Client
from clientmanager import ClientManager
from response import Response

ACTION_CLOSE_ACCOUNT = 'close_account'
ACTION_OPEN_ACCOUNT = 'open_account'
ACTION_TRANSFER = 'make_transfer'
ACTION_ACCOUNTS = 'show_accounts'
ACTION_LOGOUT = 'logout'
ACTION_LOGIN = 'login'


class SuperAction(object):

    def __init__(self):
        self.request = None
        self.manager = ClientManager()
        self.response = None

    def process(self, request):

        current_page = request.page

        if request.action == ACTION_LOGIN:
            self.response = self.login_client(request)
        elif request.action == ACTION_LOGOUT:
            client_name = request.parameters['name']
            if self.manager.logout(client_name):
                self.response = self.response.create_login()
            else:
                self.response = Response(page=current_page)
        elif request.action == ACTION_ACCOUNTS:
            client_name = request.parameters['name']
            accounts = self.manager.get_accounts(name=client_name)
            self.response = self.response.create_client(data=accounts)
        elif request.action == ACTION_TRANSFER:
            pass
        elif request.action == ACTION_OPEN_ACCOUNT:
            pass
        elif request.action == ACTION_CLOSE_ACCOUNT:
            pass

        return self.response

    def login_client(self, request):
        client_name = request.parameters['name']
        client_pass = request.parameters['pass']
        if self.manager.login(client_name, client_pass):
            response = Response.create_client()
        else:
            response = Response.create_login()
        return response



