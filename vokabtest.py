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
        self.wortlist = ['Bauklötze','arglos','verstecken','werfen','Beziehung',
                         'Erziehung','hauptsächlich','bereuen','entlang','hüpfen',
                         'Zeitstahl','lila oder violett','beitreten','peinlich',
                         'schwul/lesbisch','beschweren','Gerechitigkeit','Zweifel',
                         'retten','Das Opfer','großartig','erschaffen','entführen']
        
    def entfernen(self, w):
        self.wortlist.remove(w)
        
    def dazugeben(self, w):
        self.wortlist.append(w)
        
    def pruefen(self):
        print(choice(self.wortlist))
        