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

    ballh_change=10

    ballw_change=0
    
    gameExit = False
    flag=0;
    while not gameExit:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                gameExit=True
           
        gameDisplay.fill(white)

        
        if(ballh>=height-20):
            ballh_change=-1

        if(ballh<=20):
            ballh_change=1

        ballw+=ballw_change

        ballh+=ballh_change

        pygame.draw.circle(gameDisplay, red, [int(ballw),int(ballh)],7)
        
        pygame.draw.rect(gameDisplay, black,[ width/2-110,10,220,10])
        
        pygame.draw.rect(gameDisplay, black,[ width/2-110,height-20,220,10])
        
        pygame.display.update()
            
        clock.tick(220)
        
    pygame.quit()
    
    quit()

gameloop()
