"""
DESCRIPTION: retrieve in a json representation the software information from an MX router with a REST API call. 
the output is parsed and some details are printed
the rpc get-software-information is the equivalent of 'show version'
USAGE: python junos/get_software_information_in_json.py
"""

import requests
from pprint import pprint
from requests.auth import HTTPBasicAuth

my_headers = { 'Accept': 'application/json' }

r = requests.get('http://172.30.52.152:8080/rpc/get-software-information', auth=HTTPBasicAuth('lab', 'm0naco'), headers=my_headers)

#type(r.json())
#pprint(r.json())

print "Software version: " + r.json()['software-information'][0]['junos-version'][0]['data']
print "Host-name: " + r.json()['software-information'][0]['host-name'][0]['data']
print "Product name: " + r.json()['software-information'][0]['product-name'][0]['data']
