#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 13 17:01:35 2018

@author: kevin
"""

from pathlib import Path
import subprocess
import os
import logging


uid = os.geteuid()
gid = os.getgid()

# ~/.config/autostart/spyder.desktop
files = ['~/.condarc', '~/.gitconfig', '~/.zshrc', '/usr/lib/prezto/runcoms/zpreztorc', 
         '~/.local/share/applications/spyder.desktop', '~/.pip/pip.conf',
         '~/.config/matplotlib/matplotlibrc', '/etc/yaourtrc', '/etc/pacman.conf',
         '/etc/pacman.d/mirrorlist','/opt/bin/chray.py','/opt/bin/chvps.py']

curr_dir = Path(__file__).absolute().parent
conf_dir = curr_dir.parent / 'conf'

for path in files:
    p = Path(path)
    filename = p.name
    raw = p.expanduser()
    raw_exist = raw.exists()
    sync = conf_dir / p.name
    # sync_exist = sync.exists()
    cmd = 'meld {} {}'.format(raw,sync)
    if not raw_exist:
        subprocess.run(f'sudo mkdir {raw.parent}',shell=True, executable='/usr/bin/zsh')
        subprocess.run(f'sudo chown {uid} {raw.parent}',shell=True, executable='/usr/bin/zsh')
        subprocess.run(f'sudo chgrp {gid} {raw.parent}',shell=True, executable='/usr/bin/zsh')
        subprocess.run(f'sudo touch {raw}',shell=True, executable='/usr/bin/zsh')
        subprocess.run(f'sudo chown {uid} {raw}',shell=True, executable='/usr/bin/zsh')
        subprocess.run(f'sudo chgrp {gid} {raw}',shell=True, executable='/usr/bin/zsh')
    if raw.owner() == 'root':
        subprocess.run(f'sudo {cmd}',shell=True, executable='/usr/bin/zsh')
    else:
        subprocess.run(f'{cmd}',shell=True, executable='/usr/bin/zsh')

