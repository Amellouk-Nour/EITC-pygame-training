import pygame
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
    
    for x in range(0,50):
        pygame.draw.line(screen, (255, 255,255), (0,x*pas_y), (x*pas_x,height), width=1)
            
    

    pygame.display.update()
    

pygame.quit()
