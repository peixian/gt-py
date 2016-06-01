"""
Python Wrapper for Govtrack API v2

Based off of https://github.com/cdelguercio/govtrack-python and https://github.com/markgx/govtrack-node/

"""

import json
import requests
import urllib

API_BASE = "https://www.govtrack.us/api/v2"
VALID_ENDPOINTS = ["bill", "cosponsership", "person", "role", "vote", "vote_voter", "committee", "committe_member"]
class GTPY(object):
    
    def _param_encode(self, params):
        """docstring for _param_encode"""
        
        _params = urllib.urlencode(params)
        _params = "?" + _params
        return _params

    def _call(self, params):
        """docstring for _call"""
        url = API_BASE + params
        response = requests.get(url).content
        return response.json()
    
    def get(self, endpoint, params, obj_only):
        """
        calls the passed endpoint, returns a JSON object or a list if obj_only is true
        """
        endpoint += "/"
        data = self._call(endpoint + self._param_encode(self))
        return data["objects"] if obj_only else data
        
    
    def bill(self, params, obj_only = False):
        return self.get("bill", params, obj_only)
        
    def cosponsership(self, params, obj_only = False):
        return self.get("cosponsership", params, obj_only)
    
    def person(self, params, obj_only = False):
        return self.get("person", params, obj_only)
    
    def role(self, params, obj_only = False):
        return self.get("role", params, obj_only)
    
    def vote(self, params, obj_only = False):
        return self.get("vote", params, obj_only)
        
    def vote_voter(self, params, obj_only = False):
        return self.get("vote_voter", params, obj_only)
        
    def committee(self, params, obj_only = False):
        return self.get("committee", params, obj_only)
    
    def committee_member(self, params, obj_only = False):
        return self.get("committe_member", params, obj_only)