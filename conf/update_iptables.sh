#!/bin/ash 
chnroute_url=http://ftp.apnic.net/apnic/stats/apnic/delegated-apnic-latest
curl $chnroute_url | grep ipv4 | grep CN | awk -F\| '{ printf("%s/%d\n", $4, 32-log($5)/log(2)) }' > /tmp/chnroute.txt
iptables -t nat -N V2RAY
#your VPS IP
iptables -t nat -A V2RAY -d 95.169.10.107 -j RETURN
iptables -t nat -A V2RAY -d 97.64.47.118 -j RETURN
iptables -t nat -A V2RAY -d 107.172.103.201 -j RETURN
#your china dns
#iptables -t nat -A V2RAY -d 101.6.6.6 -j RETURN
#iptables -t nat -A V2RAY -d 101.132.183.99 -j RETURN
#iptables -t nat -A V2RAY -d 193.112.15.186 -j RETURN
#iptables -t nat -A V2RAY -d 223.113.97.99 -j RETURN
#localhost
iptables -t nat -A V2RAY -d 0.0.0.0/8 -j RETURN
iptables -t nat -A V2RAY -d 10.0.0.0/8 -j RETURN
iptables -t nat -A V2RAY -d 127.0.0.0/8 -j RETURN
iptables -t nat -A V2RAY -d 169.254.0.0/16 -j RETURN
iptables -t nat -A V2RAY -d 172.16.0.0/12 -j RETURN
iptables -t nat -A V2RAY -d 192.168.0.0/16 -j RETURN
iptables -t nat -A V2RAY -d 224.0.0.0/4 -j RETURN
iptables -t nat -A V2RAY -d 240.0.0.0/4 -j RETURN

ipset create chnroute hash:net
for i in `cat /tmp/chnroute.txt`;
do
  ipset add chnroute $i
done
iptables -t nat -A V2RAY -m set --match-set chnroute dst -j RETURN
iptables -t nat -A V2RAY -p all -j REDIRECT --to-ports 1060
iptables -t nat -A PREROUTING -p all -j V2RAY
exit 0
