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
line_length=sys.argv[3]
lines=[];t=[]
for i in range(width):
    t.append(i)
    if len(t)==line_length:
        lines.append(t)
        t=[]
if len(t)!=0:lines.append(t)
del t
for r in range(height):
    for l in lines:
        pixes=list(product(l,[r]))
        colors=[original.getpixel(address) for address in pixes]
        avg_col=pix_avg(colors)
        for p in pixes:
            new_image.putpixel(p,avg_col)
new_image.save(sys.argv[2])
