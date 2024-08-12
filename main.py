"""The main gameloop
this module should not be imported anywhere
"""
import pygame
import display
import renderer
import assets
import map
# pygame setup
pygame.init()
display.init()
assets.init()
map.init()
# TODO: Make this a little smarter...
clock = pygame.time.Clock()
running = True
tiles = []

evil_guy_cooldown = 10
renderer.ui_images.append(
    [assets.entity_textures[assets.Entities.GUY],
     (pygame.display.get_surface().get_width() / 2,
      pygame.display.get_surface().get_height() / 2)])

guy_x = int(map.SIZE[0] / 2)
guy_y = int(map.SIZE[1] / 2)

evil_guy_x = int(map.SIZE[0] / 2) + 5
evil_guy_y = int(map.SIZE[1] / 2) + 6

while running:
    # poll for events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == ord('w'):
                renderer.camera_pos[1] -= 1
            elif event.key == ord('s'):
                renderer.camera_pos[1] += 1
            elif event.key == ord('a'):
                renderer.camera_pos[0] -= 1
            elif event.key == ord('d'):
                renderer.camera_pos[0] += 1

    # evil guy logic
    if evil_guy_cooldown > 0:
        evil_guy_cooldown -= 1
    else:
        evil_guy_cooldown = 10
        diff_x = evil_guy_x - guy_x
        diff_y = evil_guy_y - guy_y

        if abs(diff_x) >= abs(diff_y):
            if diff_x != 0:
                evil_guy_x -= diff_x / abs(diff_x)
        else:
            if diff_y != 0:
                evil_guy_y -= diff_y / abs(diff_y)

    renderer.entity_list = []
    renderer.entity_list.append([assets.entity_textures[assets.Entities.GUY],
                                (guy_x, guy_y)])
    renderer.entity_list.append([assets.entity_textures[assets.Entities.EVIL_GUY],
                                (evil_guy_x, evil_guy_y)])

    renderer.render()
    clock.tick(60)  # limits FPS to 60

pygame.quit()
