from pymongo import MongoClient, ReturnDocument
import os
import sys


class BaseProviderObject(object):
    _provider_type = None
    DEBUG = (
        os.environ.get('FLASK_DEBUG') == "1" or
        "--debug" in sys.argv
    )

    def __init__(self, *args, **kwargs):
        pass

    @property
    def provider_type(self):
        if self._provider_type:
            return self._provider_type
        raise NotImplementedError

    @provider_type.setter
    def provider_type(self, prov_type):
        self._provider_type = prov_type

    def print_debug(self, *args):
        if self.DEBUG:
            print('BASE PROVIDER DEBUG:::', '\n'.join(args))
