#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  broadcom-wl.py
#
#  Copyright 2013 Antergos
#
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.

""" Broadcom-wl driver installation """

from hardware import Hardware

DEVICES = [('0x14e4', '0x4315')]

CLASS_NAME = "Broadcom_wl"

class Broadcom_wl(Hardware):
    def __init__(self):
        pass

    def get_packages(self):
        return [ "broadcom-wl" ]

    def post_install(self, dest_dir):
        pass

    def check_device(self, device):
        """ Device is (VendorID, ProductID) """
        if device in DEVICES:
            return True
        return False
        
