#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun  8 17:31:14 2020

@author: Francesco
"""


def problem3_4(mon, day, year):
    
    month = {"January":1, "February":2, "March":3, "April":4, "May":5, "June":6, "July":7,
                  "August":8, "September":9, "October":10, "November":11, "December":12}
    
    print(str(month[mon]), str(day), year, sep='/')
  
    