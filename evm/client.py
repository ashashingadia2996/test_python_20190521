from .http_client import HttpClient

# Assign all the api classes
from .api.evm import Evm


class Client(object):

    def __init__(self, auth={}, options={}):
        self.http_client = HttpClient(auth, options)

    def evm(self):
        """Evm Class for email verification
        """
        return Evm(self.http_client)

