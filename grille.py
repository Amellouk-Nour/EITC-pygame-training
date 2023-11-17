import pygame
# Initialize Pygame
pygame.init()
# Set up display
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Grille")
Running = True
# Main game loop
pas_x = width / 20
pas_y = height / 15
while Running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            Running = False
    
    for x in range(0,20):
        for y in range(0,15):
            pygame.draw.line(screen, (255, 255,255), (x*pas_x,y*pas_y), (x*pas_x + width,y*pas_y), width=1)
            pygame.draw.line(screen, (255, 255,255), (x*pas_x,y*pas_y), (x*pas_x, y*pas_y + height), width=1)
    

    pygame.display.update()
    

pygame.quit()
