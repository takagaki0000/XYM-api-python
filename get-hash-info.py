import requests
import json
import sys
args = sys.argv

url = 'https://catapult-test.opening-line.jp:3001'
#api = 'account/transfers/'
api = 'account/'

api2 = '/transaction/'
api3 = '/status'
hash = args[1]

r = requests.get(url + api2 + hash + api3 ).json()
print(url + api2 + hash + api3)

print('get-data from hash')

print(json.dumps(r,indent=4))