#!/usr/bin/env python3
# Fetch Xfce4 git repositories
# created: 20190519
# version: 0.1
# @author: kevin.bowen@gmail.com

import os

build_list = ['libxfce4util', 'xfconf', 'libxfce4ui', 'garcon', 'exo',
                'xfce4-panel', 'thunar', 'xfce4-settings',
                'xfce4-session', 'xfdesktop', 'xfwm4', 'xfce4-appfinder']

for item in build_list:
    os.system('git clone git://git.xfce.org/xfce/' + item)
