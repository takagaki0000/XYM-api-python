import requests
import json


url  = 'http://api-xym-3-01.ap-southeast-1.nemtech.network:3000/'
#api = 'account/transfers/'
api = 'account/'
account = 'DAD16D3D9B5113618F5FDA90480A062B4AB9C4FD27F3319C87F609BD3773B30B' #publickey
address = 'TBBYUQ2HYY7YYCU6LZPIRBEO57XFCOOANLXVYAH6'

r = requests.get(url + api + address ).json()
print(url + api + address )
s = requests.get(url + api + account ).json()
print(url + api + account )

print('account-info from address')

print(json.dumps(r,indent=4))

print('account-info from public-key')

print(json.dumps(s,indent=4))


