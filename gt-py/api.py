"""
Python Wrapper for Govtrack API v2

Based off of https://github.com/cdelguercio/govtrack-python and https://github.com/markgx/govtrack-node/

"""

import json
import requests
import urllib

API_BASE = "https://www.govtrack.us/api/v2"

class GTPY(object):
    
    def _param_encode(self):
        """docstring for _param_encode"""
    pass
    
    def _call(self, params):
        """docstring for _call"""
        url = API_BASE + params
        response = requests.get(url).content
        return response.json()
    
    def bill(self, params, obj_only = False):
        """
        returns JSON object for a bill or a list if obj_only is set to true
        format: https://www.govtrack.us/developers/api#endpoint_bill
        """
        data = self._call("bill/" + self._param_encode(self))
        return data["objects"] if obj_only else data
        
    def cosponsership(self, params, obj_only = False):
        """
        returns JSON object for a cosponsership or a list if obj_only is set to true
        format: https://www.govtrack.us/developers/api#endpoint_cosponsorship
        """
    pass
    
    def person(self, params, obj_only = False):
        """
        returns JSON object for a person or a list if obj_only is set to true
        format: https://www.govtrack.us/developers/api#endpoint_person
        """
    pass
    
    def role(self, params, obj_only = False):
        """
        returns JSON object for a role or a list if obj_only is set to true
        format: https://www.govtrack.us/developers/api#endpoint_role
        """
    pass
    
    def vote(self, params, obj_only = False):
        """
        returns JSON object for a vote or a list if obj_only is set to true
        format: https://www.govtrack.us/developers/api#endpoint_vote
        """
    pass
    
    def voter_voter(self, params, obj_only = False):
        """
        returns JSON object for a voter or a list if obj_only is set to true
        format: https://www.govtrack.us/developers/api#endpoint_voter
        """
    pass
    
    def committee(self, params, obj_only = False):
        """
        returns JSON object for a committee or a list if obj_only is set to true
        format: https://www.govtrack.us/developers/api#endpoint_committee
        """
    pass
    
    def committee_member(self, params, obj_only = False):
        """
        returns JSON object for a committee_member or a list if obj_only is set to true
        format: https://www.govtrack.us/developers/api#endpoint_committee_member
        """
    pass