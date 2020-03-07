import requests
import json
import codecs
import base64
import binascii

url = 'http://118.27.24.188:3000/'
#api = '/account/transfers/'
api = 'account/'
account ='5DC19A72F2C96C18DBF4477CED93F7796B452E939C0E1BBF3035C1BCB48884F0'
address='TAAWHCPS4JVBLDWEOELGI45SQD5F64URDADR5NG5'
tail = '/transactions/outgoing'
tail2 = '/transactions/incoming'

r = requests.get(url + api + address  ).json()
#r2 = requests.get(url + api  ).json()
r3 = requests.get(url + api + address  + tail).json()
q1 = requests.get(url + api + address  + tail2).json()

print(url + api + address  + tail)
print('account-data from address')
print(json.dumps(r,indent=4))
print('outgoing data')
#print(json.dumps(r2,indent=4))
print(json.dumps(r3,indent=4))

#max=len(r3)
#for n in range(0,max):
n=0
print("n:",n)
print("meta.height:{}".format(r3[n]['meta']['height']))
print("meta.id:{}".format(r3[n]['meta']['id']))
print("transaction.signer:{}".format(r3[n]['transaction']['signerPublicKey']))
print("transaction.recipient:{}".format(r3[n]['transaction']['recipientAddress']))
print("{}".format(r3[n]['transaction']['recipientAddress']))
rhex="{}".format(r3[n]['transaction']['recipientAddress'])
e = base64.b32encode(binascii.unhexlify(rhex)).decode()
print(e)

#    print(base64.b32encode(bytearray(rhex, 'ascii')).decode('utf-8'))
#    print(base64.b32encode(rhex).decode('utf-8'))
#    print(len(base64.b32encode(bytearray(rhex, 'ascii')).decode('utf-8')))
#    print(base64.b32encode(bytearray(int(rhex,16), 'ascii')).decode('utf-8'))
#    recipient = base64.b32encode(rhex)
#    print(recipient)

#print(format(r[n]['id']))
#print('signer: {}'.format(r['signer']))
#print('mosaics:{}'.format(r['mosaics']))

print("last.id:{}".format(r3[n]['meta']['id']))
lastid = r3[n]['meta']['id']

#compare id incoming

max2 = len(q1)
for m in range(0,max2):
  
	print("meta.id:{}".format(q1[m]['meta']['id']))
	print(lastid)
	if lastid > q1[m]['meta']['id'] :
		print('data is old')
	else :
		print('data is new')
		print('send mosaic to ',e)
