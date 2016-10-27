import pygame
pygame.init()
width=600
height=600
gameDisplay = pygame.display.set_mode((width,height))
pygame.display.set_caption('block game')
white=[255,255,255]
black=[0,0,0]
red=[255,0,0]
blue=[0,0,255]

pygame.display.update()

def gameloop():
    gameExit = False
    while not gameExit:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                gameExit=True
                
        gameDisplay.fill(white)

        pygame.draw.rect(gameDisplay, black,[ width/2-110,10,220,10])

        pygame.draw.rect(gameDisplay, black,[ width/2-110,height-20,220,10])

        pygame.display.update()
    pygame.quit()
    quit()

gameloop()
