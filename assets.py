import pygame
import display
from enum import IntEnum


def load_square_texture(name):
    global textures
    texture = pygame.image.load("assets/"+name+".png")
    texture = pygame.transform.scale(texture, (display.TILE_WIDTH, display.TILE_HEIGHT))
    texture.convert()
    return texture


class Tiles(IntEnum):
    MISSING = 0
    BLUE = 1
    BROWN = 2
    GREEN = 3


class Entities(IntEnum):
    MISSING = 0
    GUY = 1
    EVIL_GUY = 2


def init():
    global tile_textures
    global entity_textures
    tile_textures = [load_square_texture(a.name) for a in Tiles]
    entity_textures = [load_square_texture(a.name) for a in Entities]
