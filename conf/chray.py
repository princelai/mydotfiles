#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 28 13:58:17 2018

@author: kevin
"""

import pexpect
import logging
from pathlib import Path


logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)


class ChangeV2ray:
    def __init__(self):
        option = {1:'shadowsocks',2:'h2-tls',3:'dynamicport'}
        self.server = {"kvmcn2":"ssh -p 28777 root@lunarch.top",
                       "kvmqnet":"ssh -p 28777 root@solarck.top"}
        self.scpcmd = {"kvmcn2":"scp -P 28777 {} root@lunarch.top:/etc/v2ray/",
                       "kvmqnet":"scp -P 28777 {} root@solarck.top:/etc/v2ray/"}
        key_num = int(input('Please select fq method:\n\t1).shadowsocks\n\t2).h2-tls\n\t3).dynamic-port\n'))
        self.new_service_prefix = option.get(key_num)
        p = Path('~/.config/dotfiles/conf').expanduser()
        # dir_files = os.listdir(os.path.expanduser('~/.config/dotfiles'))
        self.client_files = [str(i) for i in p.iterdir() if i.name.endswith('client.json')]
        self.server_files = [str(i) for i in p.iterdir() if i.name.endswith('server.json')]

    def __call__(self):
        self.cp_files_client()
        self.cp_files_server()
        self.handle_client()
        self.handle_server()

    def cp_files_client(self):
        logging.info('copy files at client')
        child = pexpect.spawn('zsh -c "su root"')
        child.expect('[pP]assword:')
        child.sendline("Kai&&SMM214")
        child.expect('\[.+\][#$]')
        child.sendline(f"yes | cp -f {' '.join(self.client_files)} /etc/v2ray/")
        child.expect('\[.+\][#$]')
        child.close()

    def cp_files_server(self):
        logging.info('copy files at server')
        for k,cmd in self.scpcmd.items():
            child = pexpect.spawn('bash')
            child.expect('\[.+\][#$]')
            child.sendline(cmd.format(' '.join(self.server_files)))
            child.expect('\[.+\][#$]')
            child.close()

    #for client
    def handle_client(self):
        
        #change to root
        child = pexpect.spawn('zsh -c "su root"')
        child.expect('[pP]assword:')
        child.sendline("Kai&&SMM214")
        child.expect('\[.+\][#$]')
        #stop
        logging.info('stop service at client')
        child.sendline("systemctl |grep v2ray@ |awk '{print $1}'")
        child.expect('\[.+\][#$]')
        try:
            client_name = child.after.decode('utf8').strip().split('\r\n')[1]
        except:
            client_name = ''
        child.sendline(f"systemctl stop {client_name}")
        child.expect('\[.+@.+\][#$]')
        child.sendline(f"systemctl disable {client_name}")
        child.expect('\[.+@.+\][#$]')
        #restart
        logging.info('restart service at client')
        child.sendline(f"systemctl start v2ray@{self.new_service_prefix}-client.service")
        child.expect('\[.+@.+\][#$]')
        child.sendline(f"systemctl enable v2ray@{self.new_service_prefix}-client.service")
        child.expect('\[.+@.+\][#$]')
        child.close()
    
    #for server
    #befor enable v2ray ,you need manul stop and disable shadowsocks-libev by command:
    #systemctl stop shadowsocks-libev.service
    #systemctl disable shadowsocks-libev.service
    def handle_server(self):
        for k,v in self.server.items():
            child = pexpect.spawn(f'zsh -c "{v}"')
            child.expect('.+@.+[#$]')
            #stop current service
            logging.info('stop service at server')
            child.sendline("systemctl |grep v2ray@ |awk '{print $1}'")
            child.expect('.+@.+[#$]')
            try:
                service_name = child.before.decode('utf8').strip().split('\r\n')[1]
            except:
                service_name = ''
            child.sendline(f"systemctl stop {service_name}")
            child.expect('.+@.+[#$]')
            child.sendline(f"systemctl disable {service_name}")
            child.expect('.+@.+[#$]')
            #start new service
            logging.info('restart service at server')
            child.sendline(f"systemctl start v2ray@{self.new_service_prefix}-server.service")
            child.expect('.+@.+[#$]')
            child.sendline(f"systemctl enable v2ray@{self.new_service_prefix}-server.service")
            child.expect('.+@.+[#$]')
            self.logout(child)
                     
    def logout(self,child):
        while True:
            child.sendline('exit')
            i = child.expect(['.+@.+[#$]','logout'])
            if i == 0:
                continue
            else:
                logging.info('Connection closed.')
                child.close()
                break

if __name__ == "__main__":
    chray = ChangeV2ray()
    chray()
