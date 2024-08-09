"""The main gameloop
this module should not be imported anywhere
"""
import pygame
import display
import random
import assets
# pygame setup
pygame.init()
display.init()
assets.init()
# TODO: Make this a little smarter...
clock = pygame.time.Clock()
running = True
tiles = []

evil_guy_cooldown = 10
display.ui_images.append(
    [assets.entity_textures[assets.Entities.GUY],
     (display.window.get_width() / 2,
      display.window.get_height() / 2)])

# might want to use arrays instead of lists
tile_map = []
MAP_SIZE = (100, 100)
dir_x = [0,  0, -1,  1]
dir_y = [1, -1,  0,  0]


# generate map
for i in range(MAP_SIZE[0]):
    tile_map.append([])
    for j in range(MAP_SIZE[1]):
        tile_map[i].append(assets.tile_textures[assets.Tiles.BLUE])
current_x = int(MAP_SIZE[0] / 2)
current_y = int(MAP_SIZE[1] / 2)

for i in range(200):
    tmp = random.randrange(0, 4)
    current_x += dir_x[tmp]
    current_y += dir_y[tmp]
    for (x, y) in zip(dir_x, dir_y):
        tile_map[current_x + x][current_y + y] = assets.tile_textures[assets.Tiles.BROWN]
    tile_map[current_x][current_y] = assets.tile_textures[assets.Tiles.BROWN]

camera_x = int((MAP_SIZE[0] / 2) - (display.SCREEN_TILE_WIDTH / 2))
camera_y = int((MAP_SIZE[1] / 2) - (display.SCREEN_TILE_HEIGHT / 2))
for i in range(display.SCREEN_TILE_WIDTH):
    display.tile_screen.append([])
    for j in range(display.SCREEN_TILE_HEIGHT):
        display.tile_screen[i].append(assets.tile_textures[assets.Tiles.BLUE])

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
                display.tile_screen[i][j] = assets.tile_textures[assets.Tiles.MISSING]

    display.entity_list = []
    display.entity_list.append([assets.entity_textures[assets.Entities.GUY],
                                (guy_x - camera_x, guy_x - camera_y)])
    display.entity_list.append([assets.entity_textures[assets.Entities.EVIL_GUY],
                                (evil_guy_x - camera_x, evil_guy_y - camera_y)])

    display.render()
    clock.tick(60)  # limits FPS to 60

pygame.quit()
