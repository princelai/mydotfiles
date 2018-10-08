#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 13 17:01:35 2018

@author: kevin
"""

import logging
import os
import subprocess
from pathlib import Path

uid = os.geteuid()
gid = os.getgid()

files = [
    '~/.condarc', '~/.gitconfig', '~/.zshrc',
    '/usr/lib/prezto/runcoms/zpreztorc',
    '~/.local/share/applications/spyder.desktop', '~/.pip/pip.conf',
    '~/.config/matplotlib/matplotlibrc', '/etc/yaourtrc', '/etc/pacman.conf',
    '/etc/pacman.d/mirrorlist', '/opt/bin/chray.py', '/opt/bin/chvps.py',
    '/usr/lib/systemd/system/v2ray@.service',
    '/usr/lib/systemd/system/shadowsocks-libev@.service',
    '/usr/lib/systemd/system/haproxy@.service', '/etc/haproxy/shadowsocks.cfg',
    '/etc/haproxy/haproxy.cfg', '/etc/shadowsocks/Shadowsocks-haproxy.json','/opt/bin/zsh_history_fix'
]

curr_dir = Path(__file__).absolute().parent
conf_dir = curr_dir.parent / 'conf'

for path in files:
    p = Path(path)
    filename = p.name
    raw = p.expanduser()
    raw_exist = raw.exists()
    sync = conf_dir / p.name
    # sync_exist = sync.exists()
    cmd = 'meld {} {}'.format(raw, sync)
    if not raw_exist:
        subprocess.run(
            f'kdesu -c "mkdir {raw.parent}"',
            shell=True,
            executable='/usr/bin/zsh')
        subprocess.run(
            f'kdesu -c "chown {uid} {raw.parent}"',
            shell=True,
            executable='/usr/bin/zsh')
        subprocess.run(
            f'kdesu -c "chgrp {gid} {raw.parent}"',
            shell=True,
            executable='/usr/bin/zsh')
        subprocess.run(
            f'kdesu -c "touch {raw}"', shell=True, executable='/usr/bin/zsh')
        subprocess.run(
            f'kdesu -c "chown {uid} {raw}"',
            shell=True,
            executable='/usr/bin/zsh')
        subprocess.run(
            f'kdesu -c "chgrp {gid} {raw}"',
            shell=True,
            executable='/usr/bin/zsh')
    if raw.read_text() == sync.read_text():
        pass
    else:
        if raw.owner() == 'root':
            subprocess.run(
                f'kdesu -c "{cmd}"', shell=True, executable='/usr/bin/zsh')
        else:
            subprocess.run(f'{cmd}', shell=True, executable='/usr/bin/zsh')
