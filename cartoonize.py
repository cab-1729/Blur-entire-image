from PIL import Image
import sys
from itertools import repeat
original=Image.open(sys.argv[1])
new_image=Image.new('RGB',original.size)
width,height=original.size
da=sys.argv[3]
if da.count('-')==0:
    degree=tuple(repeat(int(da),3))
else:
    degree=tuple([int(i) for i in da.split('-')])
def color_pix(pixes,color):
    for i in pixes:
        new_image.putpixel(i,color)
def for_each_pixel(func):
    for r in range(height):
        for c in range(width):
            address=(c,r)
            color=original.getpixel(address)
            func(address,color)
def pix_avg(pixes):
    rs,gs,bs=0,0,0
    for x,y,z in pixes:
        rs+=x
        gs+=y
        bs+=z
    stuff=len(pixes)
    return (rs//stuff,gs//stuff,bs//stuff)
already_found=[]
categories={}
def sort_pixels(address,color):
    global categories
    key_val=str([i//j for i,j in zip(color,degree)])
    if key_val in already_found:
        category=categories[key_val]
        category['positions'].append(address)
        category['colors'].append(color)
    else:
        already_found.append(key_val)
        categories[key_val]={'positions':[address],'colors':[color]}
for_each_pixel(sort_pixels)
for cutout in categories.values():
    color_pix(cutout['positions'],pix_avg(cutout['colors']))
if len(sys.argv)==5:#give borders to sections
    pass

new_image.save(sys.argv[2])#saving new image