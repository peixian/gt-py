"""
Python Wrapper for Govtrack API v2

Based off of https://github.com/cdelguercio/govtrack-python and https://github.com/markgx/govtrack-node/

"""

import json
import requests
import urllib

API_BASE = "https://www.govtrack.us/api/v2/"
VALID_ENDPOINTS = ["bill", "cosponsership", "person", "role", "vote", "vote_voter", "committee", "committe_member"]
class GTPY(object):
    
    def _param_encode(self, params):
        """Checks if the parameters is just the id, if it is, pass it down. Otherwise pop out the id and parse accordingly"""
        _id = None
        if type(params) == int:
            _id = params
            return _id
        else:
            params = {k: self._jsonify(v) for k, v in params.items()}
            _id = params.get("id")
            if _id:
                _params = params.pop("id")
        _params = "?" + urllib.parse.urlencode(params) if any(params) == True else ""
        _params = _id + _params if _id else _params
        return _params

    def _call(self, params):
        """docstring for _call"""
        url = API_BASE + params
        print(url)
        response = requests.get(url)
        return response.json()
    
    def get(self, endpoint, params, obj_only):
        """
        calls the passed endpoint, returns a JSON object or a list if obj_only is true
        """
        endpoint += "/"
        data = self._call(endpoint + str(self._param_encode(params)))
        return data["objects"] if obj_only else data
        
    def _jsonify(self, val):
        """Transforms python True/False into json strings, there's probably a fucntion for this already built somewhere"""
        if val == True:
            return "true"
        elif val == False:
            return "false"
        else:
            return val

    def bill(self, params, obj_only = False):
        return self.get("bill", params, obj_only)
        
    def cosponsorship(self, params, obj_only = False):
        return self.get("cosponsorship", params, obj_only)
    
    def person(self, params, obj_only = False):
        return self.get("person", params, obj_only)
    
    def role(self, params, obj_only = False):
        return self.get("role", params, obj_only)
    
    def vote(self, params, obj_only = False):
        return self.get("vote", params, obj_only)
        
    def vote_voter(self, params, obj_only = False):
        return self.get("vote_voter", params, obj_only)
        
    def committee(self, params):
        return self.get("committee", params, False)
    
    def committee_member(self, params, obj_only = False):
        return self.get("committee_member", params, obj_only)


