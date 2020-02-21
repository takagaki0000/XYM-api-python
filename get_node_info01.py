import requests
import json
import random

url = random.choice(("http://api-xym-harvest-3-01.eu-west-1.nemtech.network:3000",\
"http://api-xym-harvest-3-01.us-west-2.nemtech.network:3000","http://api-xym-3-01.us-west-2.nemtech.network:3000",\
"http://api-xym-3-01.ap-southeast-1.nemtech.network:3000"));

#api = '/account/transfers/'
#api = '/account/'
api = '/network'
api2 = '/node/info'
api3 = '/chain/height' 

print('server >>' ,url)

r = requests.get(url + api   ).json()
q = requests.get(url + api2   ).json()
s = requests.get(url + api3   ).json()


#r = requests.get(url + api + address  ).json()
#r = requests.get(url + api  ).json()
#r = requests.get(url + api + account ).json()

print('network-data')
print(json.dumps(r,indent=4))
print('server-info')
print(json.dumps(q,indent=4))
print('block-hight')
print(json.dumps(s,indent=4))
