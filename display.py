"""Handles the display and rendering of tiles
contains the main render function"""
import pygame
window = None
SCREEN_TILE_WIDTH = 64
SCREEN_TILE_HEIGHT = 36
# Although should be const, is not initialized untill the window is
TILE_WIDTH = 0
TILE_HEIGHT = 0

tile_screen = []
images_to_draw = []

def to_screen_space(coord):
    """converts a screen_tilespace tuple to screenspace tuple"""
    return (coord[0] * TILE_WIDTH,
            coord[1] * TILE_HEIGHT)


def to_screen_tile_space(coord):
    """converts a screenspace coord to a the screen_tilespace coord"""
    return (int(coord[0] / TILE_WIDTH),
            int(coord[1] / TILE_HEIGHT))


def draw_tiles(surface):
    """renders the tiles found in tile_screen"""
    for i in range(SCREEN_TILE_WIDTH):
        for j in range(SCREEN_TILE_HEIGHT):
            surface.blit(tile_screen[i][j], to_screen_space((i, j)))


def draw_images(surface):
    """renders images on top of the tiles"""
    surface.blits(images_to_draw)


def init():
    """initializes the diplay call before accessing anything else"""
    global window, TILE_WIDTH, TILE_HEIGHT
    window = pygame.display.set_mode(pygame.display.get_desktop_sizes()[0])
    TILE_WIDTH = window.get_width() / SCREEN_TILE_WIDTH
    TILE_HEIGHT = window.get_height() / SCREEN_TILE_HEIGHT
    tile_screen = []
    for i in range(SCREEN_TILE_WIDTH):
        tile_screen.append([])
        for j in range(SCREEN_TILE_HEIGHT):
            tile_screen[i].append(None)


def render():
    """Main game render function. renders entire frame"""
    window.fill("purple")
    draw_tiles(window)
    draw_images(window)
    pygame.display.flip()
