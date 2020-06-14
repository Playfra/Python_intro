#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun  8 17:02:09 2020

@author: Francesco
"""

def problem3_3(month, day, year):
    months = ['January', 'February', 'March', 'April', 'May', 'June', 'July',
              'August', 'September', 'October', 'November', 'December']

    print(str(months[month-1])+' '+ str(day)+', '+str(year))
