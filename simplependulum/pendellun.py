from cmath import cos, pi, sin
import math,pygame as py,os,sys

from pygame.locals import *

py.init()
screen=py.display.set_mode((800,700),py.RESIZABLE)
py.display.set_caption("Pendullum.exe")
clock=py.time.Clock()
pearl=py.image.load("bob.png")
len=300
angle=pi/4
bob_pos=[350,300]
origin=[395,0]
s=True

run=True
while run:
    clock.tick(60)

    if angle > -0.8:
        if s==True:
            angle -=0.01
            if angle<-0.8:
                s=False

    if angle < 0.8:
        if s==False:
            angle +=0.01
            if angle>0.8:
                s=True
            
    print(angle)

    bob_pos[0]=len * math.sin(angle) + origin[0]
    bob_pos[1]=len * math.cos(angle) + origin[1]

    for event in py.event.get():
        if event.type == py.QUIT:
            py.quit()
            sys.exit()
        if event.type==VIDEORESIZE:
            screen=py.display.set_mode((event.w,event.h),py.RESIZABLE)
    screen.fill((30,30,30))
    py.draw.line(screen,(50,50,50),(origin[0],origin[1]),(bob_pos[0]+50,bob_pos[1]),7)
    screen.blit(pearl,(bob_pos[0],bob_pos[1]))

    py.display.update()