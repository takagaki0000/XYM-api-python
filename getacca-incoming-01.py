import requests
import json
import base64
import binascii


url = 'http://api-xym-harvest-3-01.us-west-2.nemtech.network:3000/'
#api = 'account/transfers/'
api = 'account/'
account = '5DC19A72F2C96C18DBF4477CED93F7796B452E939C0E1BBF3035C1BCB48884F0' #publickey
address = 'TAAWHCPS4JVBLDWEOELGI45SQD5F64URDADR5NG5'
tail = '/transactions/incoming'

r = requests.get(url + api + address  ).json()
#r2 = requests.get(url + api  ).json()
r3 = requests.get(url + api + address + tail).json()

print(json.dumps(r,indent=4))
print(json.dumps(r3,indent=4))

for n in range(0,5):

    print('id:{}'.format(r3[n]['meta']['id']))
    print('height:{}'.format(r3[n]['meta']['height']))
    print('signer:{}'.format(r3[n]['transaction']['signerPublicKey']))
    print('recipient:{}'.format(r3[n]['transaction']['recipientAddress']))
    add = r3[n]['transaction']['recipientAddress']
    print(add)
#base64.b32encodeはbyte型を変換してくれる str型で表示するには単にdecode
#    e = base64.b32encode(binascii.unhexlify(add))  #byte型
    e = base64.b32encode(binascii.unhexlify(add)).decode() #str型

    print('recipient address = ',e)

#print(format(r['id']))
#print('signer: {}'.format(r['signer']))
#print('mosaics:{}'.format(r['mosaics']))

