# -*- coding: utf-8 -*-
"""
Created on Sun Nov 26 12:54:46 2017

@author: katsuhisa
"""

from random import choice

# Vokabtest
class Vokab:
    '''python3 class to print a random word from a list (learning German)'''
  
    def __init__(self):
        self.wortlist = ['Bauklötze','arglos','verstecken','werfen',]
        
    def entfernen(self, w):
        self.wortlist.remove(w)
        
    def dazugeben(self, w):
        self.wortlist.append(w)
        
    def test(self):
        print(choice(self.wortlist))
        