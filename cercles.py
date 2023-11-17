import pygame
import numpy as np
# Initialize Pygame
pygame.init()
# Set up display
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Grille")
Running = True
# Main game loop
pas_x = width / 50
pas_y = height / 50
while Running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            Running = False
    for k in range(36):
        pygame.draw.circle(screen, (255,255,255), (width/2 + 160 *np.cos(2*np.pi*k/36),height/2 + 160*np.sin(2*np.pi*k/36)), 80, width=1)
            
    

    pygame.display.update()
    

pygame.quit()
