import pygame
import time

pygame.init()

width=600
height=600
gameDisplay = pygame.display.set_mode((width,height))
pygame.display.set_caption('block game')
white=[255,255,255]
black=[0,0,0]
red=[255,0,0]
blue=[0,0,255]

clock=pygame.time.Clock()
t=clock.tick(20)


def gameloop():   
    ballh=height/2
    ballw=width/2
    ballh_change=1
    ballw_change=1
    bar1_x = width/2-60
    bar1_y = 10
    bar2_x = width/2-60
    bar2_y = height-20
    gameExit = False
    flag=0;
    bar1_x_change=0
    bar2_x_change=0
    while not gameExit:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                gameExit=True
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_LEFT:
                    bar1_x_change=-2
                if event.key==pygame.K_RIGHT:
                    bar1_x_change=2
                if event.key==pygame.K_q:
                    bar2_x_change=-2
                if event.key==pygame.K_e:
                    bar2_x_change=2
            if event.type==pygame.KEYUP:
                if event.key==pygame.K_LEFT:
                    bar1_x_change=0
                if event.key==pygame.K_RIGHT:
                    bar1_x_change=0
                if event.key==pygame.K_q:
                    bar2_x_change=0
                if event.key==pygame.K_e:
                    bar2_x_change=0
        gameDisplay.fill(white)
        if(ballh>=height-20):
            ballh_change=-1

        if(ballh<=20):
            ballh_change=1
        if(ballw>=width):
            ballw_change=-1

        if(ballw<=0):
            ballw_change=1

        bar1_x+=bar1_x_change

        bar2_x+=bar2_x_change

        ballw+=ballw_change

        ballh+=ballh_change

        pygame.draw.circle(gameDisplay, red, [int(ballw),int(ballh)],7)
        
        pygame.draw.rect(gameDisplay, black,[ bar1_x,bar1_y,120,10])
        
        pygame.draw.rect(gameDisplay, black,[ bar2_x,bar2_y,120,10])
        
        pygame.display.update()
            
        clock.tick(220)
        
    pygame.quit()

    quit()

gameloop()
