import pygame

pygame.init()

WIDTH = 600
HEIGHT = 600
 
screen = pygame.display.set_mode((WIDTH,HEIGHT))
screen.fill("orange")

run=True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
    pygame.display.update()