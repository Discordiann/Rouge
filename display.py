"""Handles the display and rendering of tiles
contains the main render function"""
import pygame
SCREEN_TILE_WIDTH = 64
SCREEN_TILE_HEIGHT = 36
# Although should be const, is not initialized untill the window is
TILE_WIDTH = 0
TILE_HEIGHT = 0

tile_screen: list[list[pygame.Surface]] = []
"""defines the "screen_tilespace\""""


def to_screen_space(coord):
    """converts a screen_tilespace tuple to screenspace tuple

    note:in screen_tilespace +y is up
    """
    return (coord[0] * TILE_WIDTH,
            # 0 -> max height  max-height -> 0
            (SCREEN_TILE_HEIGHT - coord[1] - 1) * TILE_HEIGHT)


def to_screen_tile_space(coord):
    """converts a screenspace coord to a the screen_tilespace coord

    note:in screen_tilespace +y is up
    """
    # same deal
    return (int(coord[0] / TILE_WIDTH),
            int((pygame.display.get_surface().get_height() - coord[1]) / TILE_HEIGHT))


def init():
    """initializes the diplay call before accessing anything else"""
    global TILE_WIDTH, TILE_HEIGHT
    window = pygame.display.set_mode(pygame.display.get_desktop_sizes()[0])
    TILE_WIDTH = window.get_width() / SCREEN_TILE_WIDTH
    TILE_HEIGHT = window.get_height() / SCREEN_TILE_HEIGHT
    tile_screen = []
    for i in range(SCREEN_TILE_WIDTH):
        tile_screen.append([])
        for j in range(SCREEN_TILE_HEIGHT):
            tile_screen[i].append(None)
