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
                         'retten','Das Opfer','großartig','erschaffen','entführen',
                         'spinn nicht rum','beschwören','Der Neid','beneiden',
                         'auslösen','aufgeben','Der Schaden','Es hat sich erledigt',
                         'gemütlich','aufsetzen','begreifen','allerdings','Duschschlauch',
                         'Tellerablage','Tellergestell','ungünstig (Bedingungen)','ärgerlich',
                         'nervig','es stellte sich heraus','aufreißen','Stirn','Ausbruch',
                         'erwürgen','Handgelenk','lebendig','beobachten','ausfallen','bloß',
                         'zurückweisen','ergeben','verzichten','erzählen','verwenden','ablenken',
                         'Wohnungsgeber','Eigentümer','Verwaltung','beauftragen']

    def entfernen(self, w):
        self.wortlist.remove(w)

    def dazugeben(self, w):
        self.wortlist.append(w)

    def pruefen(self):
        print(choice(self.wortlist))
