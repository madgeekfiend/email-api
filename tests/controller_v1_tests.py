import os
import unittest

from emai_api import app

class ApiTests(unittest.TestCase):

    RAW_EMAIL_MESSAGE = ""
    
    ###
    # Setup & Teardown
    ###

    def setUp(self):
        app.config['TESTING'] = True
        app.config['DEBUG'] = False
        self.app = app.test_client()
        self. 

    def tearDown(self):
        pass

    ##
    # Basic Unit Test
    ##

if __name__ == "__main__":
    unittest.main()



