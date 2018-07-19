#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import subprocess

# subprocess.run('./exportprogram.sh',shell=True,executable='/usr/bin/zsh')
subprocess.run(
    'yaourt -Qqtn >! ../txt/yaourt.txt', shell=True, executable='/usr/bin/zsh')
subprocess.run(
    'pip freeze >! ../txt/pip.txt', shell=True, executable='/usr/bin/zsh')
subprocess.run(
    'conda list --export >! ../txt/conda.txt',
    shell=True,
    executable='/usr/bin/zsh')

with open('../txt/conda.txt', 'r') as fconda:
    conda_list = [
        i.split('=')[0] for i in fconda.readlines() if not i.startswith('#')
    ]

with open('../txt/pip.txt', 'r') as fpip:
    pip_list = fpip.readlines()

with open('../txt/pip.txt', 'w') as fpip2:
    new_pip = []
    for prog in pip_list:
        prog_name = prog.split('==')[0].lower()
        if prog_name not in conda_list:
            new_pip.append(prog)
    fpip2.write(''.join(new_pip))

# yaourt -S --needed - < yaourt.txt
# conda install --file conda.txt
# pip install --ignore-installed  --requirement pip.txt
