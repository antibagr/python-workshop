# get full certificate chain
openssl s_client -showcerts -connect www.google.com:443 </dev/null

# Get supported ciphers
openssl ciphers 'ALL:eNULL'
nmap -sV --script ssl-enum-ciphers -p 443 www.google.co
