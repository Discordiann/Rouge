import pygame


# pygame setup
pygame.init()
# TODO: Make this a little smarter...
window = pygame.display.set_mode(pygame.display.get_desktop_sizes()[0])
clock = pygame.time.Clock()
running = True

# asset setup
tiles = []
SCREEN_TILE_WIDTH = 80  # 640 / 8
SCREEN_TILE_HEIGHT = 45  # 360 / 8
TILE_WIDTH = window.get_width() / SCREEN_TILE_WIDTH
TILE_HEIGHT = window.get_height() / SCREEN_TILE_HEIGHT
missing_texture = pygame.image.load("image.png")
missing_texture.convert()
missing_texture = pygame.transform.scale(
                    missing_texture,
                    (TILE_WIDTH, TILE_HEIGHT))
tiles.append(missing_texture)

# might want to use arrays instead of lists
tile_screen = []
for i in range(SCREEN_TILE_WIDTH):
    tile_screen.append([])
    for j in range(SCREEN_TILE_HEIGHT):
        tile_screen[i].append(missing_texture)


def to_screen_space(coord):
    return (coord[0] * TILE_WIDTH, coord[1] * TILE_HEIGHT)


def to_screen_tile_space(choord):
    return (int(choord[0] / TILE_WIDTH), int(choord[1] / TILE_HEIGHT))


def draw_tiles():
    for i in range(SCREEN_TILE_WIDTH):
        for j in range(SCREEN_TILE_HEIGHT):
            window.blit(tile_screen[i][j], to_screen_space((i, j)))


while running:
    # poll for events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    window.fill("purple")
    draw_tiles()
    pygame.display.flip()
    clock.tick(60)  # limits FPS to 60

pygame.quit()
