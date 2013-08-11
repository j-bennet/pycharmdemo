"""
This is the class we're going to use for our refactoring example.
It contains a long jumble of spaghetti code to clean up.
"""

class SuperAction(object):
    def __init__(self):
        self.request = None

    def process(self, request):
        if request.useraction == 'login':
            pass
        elif request.useraction == 'logout':
            pass
        elif request.useraction == 'show_accounts':
            pass
        elif request.useraction == 'make_transfer':
            pass



