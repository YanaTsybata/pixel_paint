import pygame
import sys

pygame.init()

# window size
WIDTH, HEIGHT = 800, 600
PALETTE_HEIGHT = 100
DRAWING_HEIGHT = HEIGHT - PALETTE_HEIGHT

# pixel size
PIXEL_SIZE = 20

# colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# window creation
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Пиксельный художник")

# Creating a drawing surface
drawing_surface = pygame.Surface((WIDTH, DRAWING_HEIGHT))
drawing_surface.fill(WHITE)

# Creating a surface for the palette
palette_surface = pygame.Surface((WIDTH, PALETTE_HEIGHT))

current_color = BLACK
mouse_pressed = False
r, g, b = 0, 0, 0

def create_slider(x, y, width, height, color):
    slider = pygame.Rect(x, y, width, height)
    pygame.draw.rect(palette_surface, color, slider)
    return slider

r_slider = create_slider(20, 10, 260, 20, (255, 0, 0))
g_slider = create_slider(20, 40, 260, 20, (0, 255, 0))
b_slider = create_slider(20, 70, 260, 20, (0, 0, 255))

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pressed = True
        elif event.type == pygame.MOUSEBUTTONUP:
            mouse_pressed = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_c:
                drawing_surface.fill(WHITE)

    # Drawing processing
    if mouse_pressed:
        x, y = pygame.mouse.get_pos()
        if y < DRAWING_HEIGHT:  # Проверяем, что мышь в области рисования
            grid_x, grid_y = x // PIXEL_SIZE, y // PIXEL_SIZE
            pygame.draw.rect(drawing_surface, current_color, (grid_x * PIXEL_SIZE, grid_y * PIXEL_SIZE, PIXEL_SIZE, PIXEL_SIZE))

    # updating the palette
    palette_surface.fill(WHITE)
    pygame.draw.rect(palette_surface, (r, 0, 0), r_slider)
    pygame.draw.rect(palette_surface, (0, g, 0), g_slider)
    pygame.draw.rect(palette_surface, (0, 0, b), b_slider)
    pygame.draw.rect(palette_surface, current_color, (300, 10, 80, 80))

    # ПChecking interaction with the palette
    mouse_pos = pygame.mouse.get_pos()
    if DRAWING_HEIGHT <= mouse_pos[1] < HEIGHT:
        palette_y = mouse_pos[1] - DRAWING_HEIGHT
        if pygame.mouse.get_pressed()[0]:  # Левая кнопка мыши
            if r_slider.collidepoint(mouse_pos[0], palette_y):
                r = (mouse_pos[0] - r_slider.x) * 255 // r_slider.width
            elif g_slider.collidepoint(mouse_pos[0], palette_y):
                g = (mouse_pos[0] - g_slider.x) * 255 // g_slider.width
            elif b_slider.collidepoint(mouse_pos[0], palette_y):
                b = (mouse_pos[0] - b_slider.x) * 255 // b_slider.width
            current_color = (r, g, b)

    # screen, result
    screen.blit(drawing_surface, (0, 0))
    screen.blit(palette_surface, (0, DRAWING_HEIGHT))

    pygame.display.flip()

pygame.quit()
sys.exit()