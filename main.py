import pygame
import sys
import tkinter as tk
from tkinter import filedialog

root = tk.Tk()
root.withdraw()

pygame.init()

# window size
WIDTH, HEIGHT = 800, 600
PALETTE_HEIGHT = 100
DRAWING_HEIGHT = HEIGHT - PALETTE_HEIGHT

# pixel size
PIXEL_SIZE = 30

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

def draw_grid(screen):
    grid_color = (200, 200, 200)
    # vertical and horizontal lines
    for x in range(0, WIDTH, PIXEL_SIZE):
        pygame.draw.line(screen, grid_color, (x, 0), (x, DRAWING_HEIGHT))

    for y in range(0, HEIGHT, PIXEL_SIZE):
        pygame.draw.line(screen, grid_color, (0, y), (WIDTH, y))

def save_img():
    file_path = filedialog.asksaveasfilename(defaultextension=".png")
    if file_path:
        pygame.image.save(drawing_surface, file_path)

def create_slider(x, y, width, height, color):
    slider = pygame.Rect(x, y, width, height)
    pygame.draw.rect(palette_surface, color, slider)
    return slider

def draw_button(surface, text, x, y, width, height, color, text_color):
    button = pygame.Rect(x, y, width, height)
    pygame.draw.rect(surface, color, button)
    font = pygame.font.Font(None, 24)
    text_surface = font.render(text, True, text_color)
    text_rect = text_surface.get_rect(center=button.center)
    surface.blit(text_surface, text_rect)
    return button

r_slider = create_slider(20, 10, 260, 20, (255, 0, 0))
g_slider = create_slider(20, 40, 260, 20, (0, 255, 0))
b_slider = create_slider(20, 70, 260, 20, (0, 0, 255))

save_button = None

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pressed = True
            if event.button == 1:  # Left mouse button
                mouse_pos = pygame.mouse.get_pos()
                palette_y = mouse_pos[1] - DRAWING_HEIGHT
                if DRAWING_HEIGHT <= mouse_pos[1] < HEIGHT:
                    if save_button and save_button.collidepoint(mouse_pos[0], palette_y):
                        save_img()
        elif event.type == pygame.MOUSEBUTTONUP:
            mouse_pressed = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_c:
                drawing_surface.fill(WHITE)

    # Drawing processing
    if mouse_pressed:
        x, y = pygame.mouse.get_pos()
        if y < DRAWING_HEIGHT:  # Check the mouse
            grid_x, grid_y = x // PIXEL_SIZE, y // PIXEL_SIZE
            pygame.draw.rect(drawing_surface, current_color, (grid_x * PIXEL_SIZE, grid_y * PIXEL_SIZE, PIXEL_SIZE, PIXEL_SIZE))

    # updating the palette
    palette_surface.fill(WHITE)
    pygame.draw.rect(palette_surface, (r, 0, 0), r_slider)
    pygame.draw.rect(palette_surface, (0, g, 0), g_slider)
    pygame.draw.rect(palette_surface, (0, 0, b), b_slider)
    pygame.draw.rect(palette_surface, current_color, (300, 10, 80, 80))

    save_button = draw_button(palette_surface, "Save", 400, 30, 80, 30, (200, 200, 200), BLACK)

    # Checking interaction with the palette
    mouse_pos = pygame.mouse.get_pos()
    if DRAWING_HEIGHT <= mouse_pos[1] < HEIGHT:
        palette_y = mouse_pos[1] - DRAWING_HEIGHT
        if pygame.mouse.get_pressed()[0]:  # left mouse button
            if r_slider.collidepoint(mouse_pos[0], palette_y):
                r = (mouse_pos[0] - r_slider.x) * 255 // r_slider.width
            elif g_slider.collidepoint(mouse_pos[0], palette_y):
                g = (mouse_pos[0] - g_slider.x) * 255 // g_slider.width
            elif b_slider.collidepoint(mouse_pos[0], palette_y):
                b = (mouse_pos[0] - b_slider.x) * 255 // b_slider.width
            current_color = (r, g, b)

    # screen, result
    screen.blit(drawing_surface, (0, 0))
    draw_grid(screen)
    screen.blit(palette_surface, (0, DRAWING_HEIGHT))

    pygame.display.flip()

pygame.quit()
sys.exit()