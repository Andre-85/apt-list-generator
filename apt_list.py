#!/usr/bin/python3

import distro_info

suffixes = ["", "security", "updates"]
suffixes_extra = ["backports", "proposed" ]

for d in distro_info.UbuntuDistroInfo().all:
    print(d)
