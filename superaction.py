"""
This is the class we're going to use for our refactoring example.
It contains spaghetti code to clean up.
"""

class SuperAction(object):
    def __init__(self):
        self.request = None

    def process(self, request):
        if request.action == 'login':
            pass
        elif request.action == 'logout':
            pass
        elif request.action == 'show_accounts':
            pass
        elif request.action == 'make_transfer':
            pass
        elif request.action == 'open_account':
            pass
        elif request.action == 'close_account':
            pass



