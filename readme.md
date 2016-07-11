gt-py
==========

A Python wrapper for the GovTrack API (v2).

Based off of:
- [https://github.com/cdelguercio/govtrack-python](https://github.com/cdelguercio/govtrack-python)
- [https://github.com/markgx/govtrack-node/](https://github.com/markgx/govtrack-node/)

Installation
--------------
	
	pip install gt-py

Usage
-------------
	
	from gtpy.api import GTPY
	client = GTPY()

Choose an endpoint:
	
	client.role()
	client.person()
	client.cosponsorship()
	client.vote
	client.bill()
	client.vote_voter()
	client.committee()
	client.committee_member()

Get a person:

	>>>PERSON_ID = 400045
	>>>client.person(PERSON_ID)
	{'birthday': '1952-10-20', 'link': 'https://www.govtrack.us/congress/members/jeb_bradley/400045', 'lastname': 'Bradley'...
	
Filter the results, such as getting all the bills voted by the 144th Congress (supports filtering on all [filterable fields](https://www.govtrack.us/developers/api)):

	>>>CONGRESS_ID = 114
	>>>client.bill({'congress': CONGRESS_ID})
	
Change the maximum number of results:

	>>>client.bill({'congress': CONGRESS_ID, 'limit': 100})
	
	

