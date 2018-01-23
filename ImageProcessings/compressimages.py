# coding: utf-8
# compress images such that maximum pixel size will be the given value.

from os import listdir
from PIL import Image
import sys

param = sys.argv
max_px = 800
path = param[1]

photos = listdir(path)

#def compress(max_px,path,photos):
for photo in photos:
    print(max_px)
    img = Image.open(path + "/" + photo)
    sz = img.size

    comp_rate = max_px/max(sz)
    if sz[0]>sz[1]:
       newimg = img.resize((max_px,round(sz[1]*comp_rate)))
    else:
       newimg = img.resize((round(sz[0]*comp_rate),max_px))

    newimg.save(path + "/" + photo)
    print(photo + " was compressed and saved.")
