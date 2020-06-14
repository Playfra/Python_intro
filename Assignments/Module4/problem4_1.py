#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun 13 16:15:16 2020

@author: Francesco
"""

firstline = ["Happy", "families", "are", "all", "alike;", "every", \
              "unhappy", "family", "is", "unhappy", "in", "its", "own", \
              "way.", "Leo Tolstoy", "Anna Karenina"] 
#%%

def problem4_1(wordlist):
   
    print(wordlist)
    wordlist.sort(key=str.lower)
    print(wordlist)
    