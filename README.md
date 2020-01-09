certbot manual auth hook for godaddy   


crontab -l . 
`
00 00 * * * certbot renew --manual-auth-hook /etc/letsencrypt/renewal-hooks/pre/godaddy-authenticator.sh --cert-name yourcertname
`
