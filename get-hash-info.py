import requests
import json
import sys
args = sys.argv

url = 'http://api-xym-harvest-3-01.eu-west-1.nemtech.network:3000/'
#api = 'account/transfers/'
api = 'account/'

api2 = '/transaction/'
api3 = '/status'
hash = args[1]

r = requests.get(url + api2 + hash + api3 ).json()
print(url + api2 + hash + api3)

print('get-data from hash')

print(json.dumps(r,indent=4))
