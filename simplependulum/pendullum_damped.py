from cmath import cos, pi, sin
import math,pygame as py,os,sys,time

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
acc=0
vel=0
gravity=0.005
friction=0
start = time.time()

run=True
while run:
    clock.tick(60)
    force=gravity*math.sin(angle)
    acc=-force
    vel+=acc
    angle+=vel
    vel*=0.999
    end = time.time()
    timepass=int(end-start)
    #print(vel)
    #print(timepass)
    #if timepass%30==0:
    #    vel=0
    #    angle=pi/4

    #print(angle)

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