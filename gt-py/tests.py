from unittest2 import TestCase

from api import GTPY

class GTPYTests(TestCase):
    def setUp(self):
        self.client = GTPY()
    
    def test_url_encode(self):
        #encoding a regular dictionary w/o an id
        test_params = {'lastname': 'Kennedy'}
        encodeTest = self.client._param_encode(test_params)
        self.assertEqual(encodeTest, "?lastname=Kennedy")
        
        #encoding an id
        test_params = {"id": "40054"}
        encodeTest = self.client._param_encode(test_params)
        self.assertEqual(encodeTest, "40054")
        
        #encoding an id and other values
        test_params = {"id": "40054", "lastname": "Kennedy"}
        encodeTest = self.client._param_encode(test_params)
        self.assertEqual(encodeTest, "40054?lastname=Kennedy")