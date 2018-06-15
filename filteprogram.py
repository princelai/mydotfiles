#!/usr/bin/env python3
# -*- coding: utf-8 -*-


with open('conda.txt','r') as fconda:
    conda_list = [i.split('=')[0] for i in fconda.readlines() if not i.startswith('#')]

with open('pip.txt','r') as fpip:
    pip_list = fpip.readlines()
    
with open('pip.txt','w') as fpip2:
    new_pip = []
    for prog in pip_list:
        prog_name = prog.split('==')[0].lower()
        if prog_name not in conda_list:
            new_pip.append(prog)
    fpip2.write(''.join(new_pip))

