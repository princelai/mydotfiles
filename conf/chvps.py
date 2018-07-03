#!/usr/bin/python

import subprocess
from subprocess import PIPE

option_obfs = {1:'shadowsocks-libev',2:'shadowsocks-libev-http',3:'shadowsocks-libev-tls'}
option_server = {1:'bwh_kvm.service',2:'bwh_ovz.service',3:'virmach.service'}

obfs = int(input('Please select obfs method:\n\t1).non-obfs\n\t2).obfs-http\n\t3).obfs-tls\n'))
server = int(input('Please select server:\n\t1).bwh_kvm\n\t2).bwh_ovz\n\t3).virmach\n'))

select_obfs = option_obfs.get(obfs)
select_server = option_server.get(server)

#kill current ss service
get_ss_service = subprocess.run("systemctl |grep shadowsocks-libev |awk '{print $1}'",check=True,stdout=PIPE,shell=True,executable='/usr/bin/zsh')
current_ss_service = get_ss_service.stdout.decode('utf8').strip()
#kill & disable current ss service
subprocess.run(f'sudo systemctl stop {current_ss_service}',shell=True,executable='/usr/bin/zsh')
subprocess.run(f'sudo systemctl disable {current_ss_service}',shell=True,executable='/usr/bin/zsh')
#reopen
subprocess.run(f'sudo systemctl start {select_obfs}@{select_server}',shell=True,executable='/usr/bin/zsh')
subprocess.run(f'sudo systemctl enable {select_obfs}@{select_server}',shell=True,executable='/usr/bin/zsh')