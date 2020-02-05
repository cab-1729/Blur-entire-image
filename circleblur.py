from math import sqrt
from PIL import Image
from itertools import product
import sys
class Circle:
    radius=sys.argv[3]
    diameter=2*radius
    @staticmethod
    def pix_avg(pixes):
        r,g,b=0,0,0
        l=len(pixes)
        for p in pixes:
            r+=p[0]
            g+=p[1]
            b+=p[2]
        return (r//l,g//l,b//l)
    @staticmethod
    def is_valid_pixel(position):
        if position[0]<0 or position[0]>=width or position[1]<0 or position[1]>=height:
            return False
        return True
    def __init__(self,column,row):
        self.column=column
        self.row=row
        self.center=((2*column+1)*Circle.radius+column,(2*row+1)*Circle.radius+row)
        self.members=self.get_members()
        self.color=self.get_color()
    def get_members(self):
        members=[]
        for h in range(Circle.radius+1):
            x=int(sqrt(self.radius**2-h**2))
            for j in range(x+1):
                xes=(self.center[0]+j,self.center[0]-j)
                hes=(self.center[1]+h,self.center[1]-h)
                new_points=product(xes,hes)
                for m in new_points:
                    if Circle.is_valid_pixel(m):
                        members.append(m)
        return members
    def get_color(self):
        member_colors=[original.getpixel(address) for address in self.members]
        if len(self.members)==0:
            print(self.center)
            return(255,0,0)
        return Circle.pix_avg(member_colors)
    def appear(self,img):
        for m in self.members:
            img.putpixel(m,self.color)
original=Image.open(sys.argv[1])
new_image=Image.new('RGB',original.size)
width,height=original.size
circle_row=width//(Circle.diameter+1)
circle_column=height//(Circle.diameter+1)
for r in range(circle_row):
    for c in range(circle_column):
        Circle(r,c).appear(new_image)
new_image.save(sys.argv[2])
