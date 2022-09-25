import pygame,sys

from pygame.locals import *
pygame.init()
clock = pygame.time.Clock()

pygame.display.set_caption('pulley.exe')
screen = pygame.display.set_mode((640, 640),pygame.RESIZABLE,32)

body=pygame.image.load("bob.png")

origin_a=[445,0]
bodya_pos=[400,300]
origin_b=[195,0]
bodyb_pos=[150,300]

mass_body_a=5
mass_body_b=2

gravity=0.04
vel=0

while True:
    
    screen.fill((30,30,30))
    mx, my = pygame.mouse.get_pos()

    acceleration=((mass_body_a-mass_body_b)*gravity)/(mass_body_a+mass_body_b)
    vel+=acceleration
    bodya_pos[1]+=vel
    bodyb_pos[1]-=vel
    if bodya_pos[1]>600:
        bodya_pos[1]=300
        vel=0
    if bodyb_pos[1]<0:
        bodyb_pos[1]=300
        vel=0


    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                pygame.quit()
                sys.exit()

        if event.type==VIDEORESIZE:
            screen=pygame.display.set_mode((event.w,event.h),pygame.RESIZABLE)
 
        if event.type == MOUSEBUTTONDOWN:
            if event.button == 1:
                clicking = True
 
        if event.type == MOUSEBUTTONUP:
            if event.button == 1:
                clicking = False

    pygame.draw.line(screen,(50,50,50),(origin_a[0],origin_a[1]),(bodya_pos[0]+50,bodya_pos[1]),7)
    screen.blit(body,(bodya_pos[0],bodya_pos[1]))

    pygame.draw.line(screen,(50,50,50),(origin_b[0],origin_b[1]),(bodyb_pos[0]+50,bodyb_pos[1]),7)
    screen.blit(body,(bodyb_pos[0],bodyb_pos[1]))
                
    # Update ------------------------------------------------- #
    pygame.display.update()
    clock.tick(60)
