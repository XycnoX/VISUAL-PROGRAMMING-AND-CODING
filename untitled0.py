# -*- coding: utf-8 -*-
"""
Created on Thu Jun 10 19:16:00 2021

@author: ylmzc
"""

from PyQt5 import uic

with open('GP_SON.py','w',encoding="utf-8") as fout:
    uic.compileUi('GP_SON.ui',fout)