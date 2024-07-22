import pygame
import sys

# Pygame initialisation
pygame.init()

# window size
WIDTH = 400
HEIGHT = 620

# pixel size
PIXEL_SIZE = 20

# colors
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)

# window creation
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pixel artist")

# current color
current_color = black

# mouse pressed or not
mouse_pressed = False

# cycle

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pressed = True
        elif event.type == pygame.MOUSEBUTTONUP:
            mouse_pressed =False
        elif event.type == pygame.KEYDOWN:
            #color change
            if event.key == pygame.K_r:
                current_color = red
            elif event.key == pygame.K_g:
                current_color = green
            elif event.key == pygame.K_b:
                current_color = blue
            elif event.key == pygame.K_w:
                current_color = white
            elif event.key == pygame.K_k:
                current_color = black
            if event.key == pygame.K_c:
                screen.fill(white) # clear screen

    # localisation mouse, if pressed paint
    if mouse_pressed:
        x, y = pygame.mouse.get_pos() # mouse position
        # editing coodrinates to net
        grid_x = x // PIXEL_SIZE
        grid_y = y // PIXEL_SIZE
        # pixel painting
        pygame.draw.rect(screen, current_color,(grid_x * PIXEL_SIZE, grid_y * PIXEL_SIZE, PIXEL_SIZE, PIXEL_SIZE))

    # update screen
    pygame.display.flip()

# done work
pygame.quit()
sys.exit()