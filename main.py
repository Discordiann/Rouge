"""The main gameloop
this module should not be imported anywhere
"""
import pygame
import display
import random
# pygame setup
pygame.init()
display.init()
# TODO: Make this a little smarter...
clock = pygame.time.Clock()
running = True
tiles = []

# asset setup
missing_texture = pygame.image.load("image.png")
missing_texture.convert()
missing_texture = pygame.transform.scale(
                    missing_texture,
                    (display.TILE_WIDTH, display.TILE_HEIGHT))
tiles.append(missing_texture)
brown_texture = pygame.image.load("Brown.png")
brown_texture.convert()
brown_texture = pygame.transform.scale(
                    brown_texture,
                    (display.TILE_WIDTH, display.TILE_HEIGHT))
tiles.append(brown_texture)
blue_texture = pygame.image.load("Blue.png")
blue_texture.convert()
blue_texture = pygame.transform.scale(
                    blue_texture,
                    (display.TILE_WIDTH, display.TILE_HEIGHT))

guy = pygame.image.load("guy.png")
guy.convert()
guy = pygame.transform.scale(
                    guy,
                    (display.TILE_WIDTH, display.TILE_HEIGHT))

evil_guy = pygame.image.load("evil_guy.png")
evil_guy.convert()
evil_guy = pygame.transform.scale(
                    evil_guy,
                    (display.TILE_WIDTH, display.TILE_HEIGHT))

evil_guy_cooldown = 10

# might want to use arrays instead of lists
tile_map = []
MAP_SIZE = (100, 100)
dir_x = [0,  0, -1,  1]
dir_y = [1, -1,  0,  0]

# generate map
for i in range(MAP_SIZE[0]):
    tile_map.append([])
    for j in range(MAP_SIZE[1]):
        tile_map[i].append(blue_texture)
current_x = int(MAP_SIZE[0] / 2)
current_y = int(MAP_SIZE[1] / 2)

for i in range(200):
    tmp = random.randrange(0, 4)
    current_x += dir_x[tmp]
    current_y += dir_y[tmp]
    for (x, y) in zip(dir_x, dir_y):
        tile_map[current_x + x][current_y + y] = brown_texture
    tile_map[current_x][current_y] = brown_texture

camera_x = int((MAP_SIZE[0] / 2) - (display.SCREEN_TILE_WIDTH / 2))
camera_y = int((MAP_SIZE[1] / 2) - (display.SCREEN_TILE_HEIGHT / 2))
for i in range(display.SCREEN_TILE_WIDTH):
    display.tile_screen.append([])
    for j in range(display.SCREEN_TILE_HEIGHT):
        display.tile_screen[i].append(missing_texture)

guy_x = int(MAP_SIZE[0] / 2)
guy_y = int(MAP_SIZE[1] / 2)

evil_guy_x = int(MAP_SIZE[0] / 2) + 2
evil_guy_y = int(MAP_SIZE[1] / 2) + 2

while running:
    # poll for events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == ord('w'):
                camera_y -= 1
            elif event.key == ord('s'):
                camera_y += 1
            elif event.key == ord('a'):
                camera_x -= 1
            elif event.key == ord('d'):
                camera_x += 1

    # evil guy logic
    if evil_guy_cooldown > 0:
        evil_guy_cooldown -= 1
    else:
        evil_guy_cooldown = 10
        diff_x = evil_guy_x - guy_x
        diff_y = evil_guy_y - guy_y
        
        if abs(diff_x) >= abs(diff_y):
            evil_guy_x -= diff_x / abs(diff_x)
        else:
            evil_guy_y -= diff_y / abs(diff_y)

    for i in range(display.SCREEN_TILE_WIDTH):
        for j in range(display.SCREEN_TILE_HEIGHT):
            if (0 <= i + camera_x < len(tile_map)
                    and j + camera_y < len(tile_map[0])):
                display.tile_screen[i][j] = tile_map[i + camera_x][j + camera_y]
            else:
                display.tile_screen[i][j] = missing_texture

    display.entity_list = []
    display.entity_list.append([guy, (guy_x - camera_x, guy_x - camera_y)])
    display.entity_list.append([evil_guy, (evil_guy_x - camera_x, evil_guy_y - camera_y)])

    display.render()
    clock.tick(60)  # limits FPS to 60

pygame.quit()
