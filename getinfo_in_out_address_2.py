import requests
import json
import sys
args = sys.argv


url = 'http://api-xym-harvest-3-01.eu-west-1.nemtech.network:3000/'
#api = 'account/transfers/'
api = 'account/'
account = '' #publickey
address1 = args[1]
address =address1.replace("-","")

print(address1)
print(address)

tail = '/transactions/outgoing'
tail2 = '/transactions/incoming'
r = requests.get(url + api + address  ).json()
#r = requests.get(url + api  ).json()
r1 = requests.get(url + api + address + tail+'?page=20').json()
r2 = requests.get(url + api + address + tail2+'?page=20').json()

print('account_data')
print(json.dumps(r,indent=4))

print('outgoing-data')
print(json.dumps(r1,indent=4))


print('outgoing-data')
max=len(r1)
for n in range(0,max):
    print('data-no',n)
    print('id:{}'.format(r1[n]['meta']['id']))
    print('type:{}'.format(r1[n]['transaction']['type']))
    type2 = r1[n]['transaction']['type']
#    print('type2',type2)
    print('signerPublicKey:{}'.format(r1[n]['transaction']['signerPublicKey']))
    if type2 == 16724:    
        print('recipientAddress: {}'.format(r1[n]['transaction']['recipientAddress']))
    else:
        print('recieient=null')



print('incoming-data')

print(json.dumps(r2,indent=4))


print('incoming-data')
max2=len(r2)

for m in range(0,max2):

    print('data-no',m)
    print('id:{}'.format(r2[m]['meta']['id']))
    print('signerPublicKey:{}'.format(r2[m]['transaction']['signerPublicKey']))
#    print('recipientAddress:{}'.format(r2[m]['transaction']['recipientAddress']))
#    print('type:{}'.format(r1[m]['transaction']['type']))
#    type3 = r2[m]['transaction']['type']
#    print('type3',type3)
