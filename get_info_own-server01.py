import requests
import json
import time

own_server = 'http://118.27.24.188:3000'

url = own_server + '/chain/height'
url2 = own_server + '/node/peers'
url3 = own_server + '/node/info'



r = requests.get(url).json()
r2 = requests.get(url2).json()
r3 = requests.get(url3).json()


print(json.dumps(r3,indent=4))
print(json.dumps(r,indent=4))
time.sleep(10)

print(json.dumps(r2,indent=4))

