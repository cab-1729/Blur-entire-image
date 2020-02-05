from PIL import Image
import sys
from itertools import product
original=Image.open(sys.argv[1])
new_image=Image.new('RGB',original.size)
def pix_avg(pixes):
    r,g,b=0,0,0
    l=len(pixes)
    for i in pixes:
        r+=i[0]
        g+=i[1]
        b+=i[2]
    return(r//l,g//l,b//l)
def pix_rms(pixes):
    pass
width,height=original.size
factor=int(sys.argv[3])
wpix=[];hpix=[]
t=[]
for i in range(width):
    t.append(i)
    if len(t)==factor:
        wpix.append(t)
        t=[]
if len(t)!=0:
    wpix.append(t);t=[]
for i in range(height):
    t.append(i)
    if len(t)==factor:
        hpix.append(t)
        t=[]
if len(t)!=0:
    hpix.append(t);t=[]
for r in hpix:
    for c in wpix:
        space=list(product(c,r))
        colors=[original.getpixel(address) for address in space]
        avg_col=pix_avg(colors)
        for a in space:
            new_image.putpixel(a,avg_col)
new_image.save(sys.argv[2])
