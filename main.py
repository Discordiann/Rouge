"""The main gameloop
this module should not be imported anywhere
"""
import pygame
import display

# pygame setup
pygame.init()
display.init()
# TODO: Make this a little smarter...
clock = pygame.time.Clock()
running = True

# asset setup
tiles = []
missing_texture = pygame.image.load("image.png")
missing_texture.convert()
missing_texture = pygame.transform.scale(
                    missing_texture,
                    (display.TILE_WIDTH, display.TILE_HEIGHT))
brown_texture = pygame.image.load("Brown.png")
brown_texture.convert()
brown_texture = pygame.transform.scale(
                    brown_texture,
                    (display.TILE_WIDTH, display.TILE_HEIGHT))
tiles.append(brown_texture)

# might want to use arrays instead of lists
for i in range(display.SCREEN_TILE_WIDTH):
    display.tile_screen.append([])
    for j in range(display.SCREEN_TILE_HEIGHT):
        if i > 10:
            texture = missing_texture
        else:
            texture = brown_texture
        display.tile_screen[i].append(texture)

while running:
    # poll for events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    # fill the screen with a color to wipe away anything from last frame
    display.render()
    clock.tick(60)  # limits FPS to 60

pygame.quit()
