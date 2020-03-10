## let's encrypt certbot renew with dns challenges  
certbot manual auth hook for godaddy   


crontab -l  
`
00 00 * * * certbot renew --manual-auth-hook /etc/letsencrypt/renewal-hooks/pre/godaddy-authenticator.sh --cert-name yourcertname
`

/etc/letsencrypt/renewal/xxxxx.conf. 
```
version = 0.31.0
archive_dir = xxxxx
cert = xxxx
privkey = xxxx
chain = xxx
fullchain = xxx

# Options used in the renewal process
[renewalparams]
account = xxxx
server = https://acme-v02.api.letsencrypt.org/directory
manual_public_ip_logging_ok = True
pref_challs = dns-01,
authenticator = manual
manual_auth_hook = /etc/letsencrypt/renewal-hooks/pre/godaddy-authenticator.py
```
