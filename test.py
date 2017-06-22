from urllib import urlencode
from httplib2 import Http
import json
import sys
import base64


print "Running Endpoint Tester....\n"
address = raw_input("Please enter the address of the server you want to access, \n If left blank the connection will be set to 'http://localhost:5000':   ")
if address == '':
	address = 'http://localhost:5000'

try:
	h = Http()
	url = address + '/'
	resp, content = h.request(url,'GET', headers = {"Content-Type": "application/json"})
	if resp['status'] != '200':
 		raise Exception('Received an unsuccessful status code of %s' % resp['status'])

except Exception as err:
	print "Test FAILED"
	print err.args
	sys.exit()
else:
	print "Test PASS: Succesfully"
