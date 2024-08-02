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
entity_list = []
ui_images = []


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


def draw_entities(surface):
    """renders entities found in entity_list"""
    for entity in entity_list:
        surface.blit(entity[0], to_screen_space(entity[1]))


def draw_UI(surface):
    """renders UI elements from images_to_draw on top of the tiles"""
    surface.blits(ui_images)


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
    draw_entities(window)
    draw_UI(window)
    pygame.display.flip()
