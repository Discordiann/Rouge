"""Handles the display and rendering of tiles
contains the main render function"""
import pygame
SCREEN_TILE_WIDTH = 64
SCREEN_TILE_HEIGHT = 36
# Although should be const, is not initialized untill the window is
TILE_WIDTH = 0
TILE_HEIGHT = 0


def init():
    """initializes the diplay call before accessing anything else"""
    global TILE_WIDTH, TILE_HEIGHT
    window = pygame.display.set_mode(pygame.display.get_desktop_sizes()[0])
    TILE_WIDTH = window.get_width() / SCREEN_TILE_WIDTH
    TILE_HEIGHT = window.get_height() / SCREEN_TILE_HEIGHT
