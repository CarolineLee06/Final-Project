import pygame
from pygame.locals import *


pygame.init()


width = 1000
height = 1000
pygame.display.set_caption("SquareDraw")

numberOfRows = 250  
numberOfColumns = 250
screen = pygame.display.set_mode((width, height), pygame.RESIZABLE)
grid = [[0 for x in range(numberOfRows)] for y in range(numberOfColumns)] 


basicX = width / numberOfColumns
basicY = height / numberOfRows


running = 1
clicking = 0

def drawScreen(screen, grid, basicX, basicY):  
    for i in range(numberOfColumns):
        for j in range(numberOfRows):
            if grid[i][j]:
                pygame.draw.rect(screen, (0, 0, 0), (j * basicX, i * basicY, basicX, basicY))

screen.fill((255, 255, 255))  

while running:
    events = pygame.event.get()
    for event in events:
        if (event.type == pygame.QUIT) or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
            running = 0
        if event.type == pygame.MOUSEBUTTONDOWN or clicking:  
            clicking = 1
            x, y = pygame.mouse.get_pos()
            xInGrid = int(x / basicX)
            yInGrid = int(y / basicY)
            grid[yInGrid][xInGrid] = 1 
            pygame.draw.rect(screen, (0, 0, 0), (xInGrid * basicX, yInGrid * basicY, basicX, basicY))
            pygame.display.flip()  
        if event.type == pygame.MOUSEBUTTONUP:
            clicking = 0
        if event.type == pygame.VIDEORESIZE:  
            width = event.w
            height = event.h
            basicX = width / numberOfColumns
            basicY = height / numberOfRows
            #print(width, height)
            screen = pygame.display.set_mode((width, height), pygame.RESIZABLE)  
            screen.fill((255, 255, 255)) 
            drawScreen(screen, grid, basicX, basicY) 
            pygame.display.flip()  


pygame.quit()