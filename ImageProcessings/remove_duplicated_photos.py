# -*- coding: utf-8 -*-
"""
Created on Sat Jun 16 17:56:48 2018

@author: katsuhisa
"""

from PIL import Image
import imagehash
import numpy as np
from os import listdir, remove
from os.path import isfile, join

# Maximum Hamming distance required to determine a match (0.0 - 1.0)
hamming_threshold = 0.1

# Hamming distance
def hamming(s1, s2):
    '''
    Calculate the normalized Hamming distance between two strings.
    '''
    try:
        assert len(s1) == len(s2)
        return float(sum(c1 != c2 for c1, c2 in zip(s1, s2))) / float(len(s1))
    except:
        return 1
        
# path where duplicated photos are stored
mypath = r"C:\Users\katsuhisa\Google ドライブ\myphoto"

# photos
files = [f for f in listdir(mypath) if isfile(join(mypath, f))]
lenf = len(files)
print('File names were read...')

# extract pixel velues from each image
images = [None]*lenf
for f in range(lenf):
    try:    
        dhash = imagehash.dhash(Image.open(join(mypath, files[f])).convert('LA'))
        images[f] = str(dhash)
    except:
        print(files[f] + ' is not a picture?')

print('Pixel values were extracted...')

# remove duplicated files
out = []
for f in range(lenf):
    dup = [i for i, img in enumerate(images) if hamming(images[f], img) <= hamming_threshold]
    if len(dup) > 1:
        out = out + dup[1:]
        
out = list(set(out))    
for r in out:
    print('removing file ' + files[r])
    remove(join(mypath, files[r]))

print('Duplicated images (' + str(len(out)) + '/' + str(lenf) + ') were removed')

