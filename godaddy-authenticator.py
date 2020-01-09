#!/usr/bin/python3

import os
import sys
from godaddypy import Client, Account

try:
  certDOMAIN=os.environ['CERTBOT_DOMAIN']
  certVALIDATION=os.environ['CERTBOT_VALIDATION']
except:
  sys.exit(1)

# Remember to set your parameters
paramAPIKEY = 'godaddy api key'
paramAPISECRET = 'godaddy api secret'
paramDNSNAME = 'dnsrecord name' # for wildcard = _acme-challenge'

userAccount = Account(api_key=paramAPIKEY, api_secret=paramAPISECRET)
userClient = Client(userAccount)

domain = certDOMAIN
n_record = paramDNSNAME
v_record = certVALIDATION

try:
  records = userClient.get_records(domain, name=n_record, record_type='TXT')
  print(records)
  if len(records)==0:
    userClient.add_record(domain, {'data':v_record,'name':n_record,'ttl':600, 'type':'TXT'})
  records = userClient.get_records(domain, name=n_record, record_type='TXT')
  for record in records:
    if v_record != record["data"]:
      updateResult = userClient.update_record(domain,{'data':v_record,'name':n_record,'ttl':600, 'type':'TXT'})
      if updateResult is True:
        print('Update ended with no Exception.')
      else:
        print('No DNS update needed.')
except:
  print(sys.exc_info()[1])
  sys.exit()
