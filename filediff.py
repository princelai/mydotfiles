#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 13 17:01:35 2018

@author: kevin
"""

from pathlib import Path
import subprocess


files = ['~/.condarc', '~/.gitconfig', '~/.zshrc', '/usr/lib/prezto/runcoms/zpreztorc', 
         '~/.config/autostart/spyder.desktop', '~/.pip/pip.conf',
         '~/.config/matplotlib/matplotlibrc', '/etc/yaourtrc', '/etc/pacman.conf',
         '/etc/pacman.d/mirrorlist',]

curr_dir = Path(__file__).absolute().parent
# print(curr_dir)
for path in files:
    p = Path(path)
    filename = p.name
    raw = p.expanduser()
    raw_exist = raw.exists()
    sync = p.cwd() / p.name
    sync_exist = sync.exists()
    cmd = 'meld {} {}'.format(raw,sync)
    if raw.owner() == 'root':
        subprocess.run(f'sudo {cmd}',shell=True, executable='/usr/bin/zsh')
    else:
        subprocess.run(f'{cmd}',shell=True, executable='/usr/bin/zsh')
