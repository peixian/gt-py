from unittest2 import TestCase

from api import GTPY

class GTPYTests(TestCase):
    def setUp(self):
        self.client = GTPY()
    
    def test_url_encode(self):
        #encoding a regular dictionary w/o an id
        test_params = {'lastname': 'Kennedy'}
        encode_test = self.client._param_encode(test_params)
        self.assertEqual(encode_test, "?lastname=Kennedy")

        #encoding an id
        test_params = {"id": "40054"}
        encode_test = self.client._param_encode(test_params)
        self.assertEqual(encode_test, "40054")

        #encoding an id and other values
        test_params = {"id": "40054", "lastname": "Kennedy"}
        encode_test = self.client._param_encode(test_params)
        self.assertEqual(encode_test, "40054?lastname=Kennedy")
    
    def test_role(self):
        """Tests for the role"""
        TEST_ROLE_STATUS = True
        TEST_ROLE_LIMIT = 50
        test_params = {"current": TEST_ROLE_STATUS, "limit": TEST_ROLE_LIMIT}
        response = self.client.role(test_params)
        print(response["meta"]["limit"])
        self.assertEqual(response["meta"]["limit"], TEST_ROLE_LIMIT)
        self.assertEqual(response["objects"][0]["current"], TEST_ROLE_STATUS)
    
    def test_person(self):
        """Tests for person"""
        
        TEST_ID = 400054
        
        response = self.client.person(TEST_ID)
        self.assertTrue("id" in response and response["id"] == TEST_ID) 
        self.assertTrue("name" in response and "roles" in response)