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
        #tests the status with python bools and role limits
        TEST_ROLE_STATUS = True
        TEST_ROLE_LIMIT = 50
        test_params = {"current": TEST_ROLE_STATUS, "limit": TEST_ROLE_LIMIT}
        response = self.client.role(test_params)
        self.assertEqual(response["meta"]["limit"], TEST_ROLE_LIMIT)
        self.assertEqual(response["objects"][0]["current"], TEST_ROLE_STATUS)
        
        response = self.client.role(test_params, True)
        self.assertEqual(response[0]["current"], TEST_ROLE_STATUS)
        
    def test_person(self):
        """Tests for person"""
        
        TEST_ID = 400054
        response = self.client.person(TEST_ID)
        self.assertTrue("id" in response and response["id"] == TEST_ID) 
        self.assertTrue("name" in response and "roles" in response)
        
    def test_cosponsorship(self):
        """Tests for the cosponsorship"""
        
        TEST_BILL_ID = 345256
        response = self.client.cosponsorship({"bill": TEST_BILL_ID})
        self.assertEqual(response["objects"][0]["bill"], TEST_BILL_ID)
        
        response = self.client.cosponsorship({"bill": TEST_BILL_ID}, True)
        self.assertEqual(response[0]["bill"], TEST_BILL_ID)
        
        TEST_BILL_ID = 1
        response = self.client.cosponsorship(TEST_BILL_ID)
        self.assertEqual(response["id"], TEST_BILL_ID)
        
    def test_vote(self):
        """docstring for test_vote"""
        
        TEST_VOTE_ID = 1
        response = self.client.vote(TEST_VOTE_ID)
        self.assertEqual(response["id"], TEST_VOTE_ID)
        
        TEST_VOTE_CONGRESS = 112
        TEST_VOTE_CHAMBER = "house"
        TEST_VOTE_SESSION = 2011
        response = self.client.vote({"congress": TEST_VOTE_CONGRESS, "chamber": TEST_VOTE_CHAMBER, "session": TEST_VOTE_SESSION})
        self.assertEqual(response["objects"][0]["id"], 1015)
        
        response = self.client.vote({"congress": TEST_VOTE_CONGRESS, "chamber": TEST_VOTE_CHAMBER, "session": TEST_VOTE_SESSION}, True)
        self.assertEqual(response[0]["id"], 1015)
        
    
    def test_vote_voter(self):
        """docstring for test_vote_voter"""
    pass
    
    def test_comittee(self):
        """docstring for test_comittee"""
    pass
    
    def test_committee_memember(self):
        """docstring for test_committee_memember"""
    pass