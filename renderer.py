import pygame
import display
import assets
import map

entity_list: list[list[pygame.Surface | tuple[int, int]]] = []
"""contains a list of entities, each containing their sprite and position in "screen_tilespace\""""
ui_images: list[pygame.Surface]= []
"""contains a list of images to be blitted onto the screen last each frame"""
camera_pos = [int((map.SIZE[0] / 2) - (display.SCREEN_TILE_WIDTH / 2)),
              int((map.SIZE[1] / 2) - (display.SCREEN_TILE_HEIGHT / 2))]


def draw_tiles(surface):
    """renders the tiles found in tile_screen"""
    for i in range(display.SCREEN_TILE_WIDTH):
        for j in range(display.SCREEN_TILE_HEIGHT):
            if (0 <= i + camera_pos[0] < len(map.tile_map)
                    and j + camera_pos[1] < len(map.tile_map[0])):
                surface.blit(
                    map.tile_map[i + camera_pos[0]][j + camera_pos[1]],
                    display.to_screen_space((i, j))
                )
            else:
                surface.blit(
                    assets.tile_textures[assets.Tiles.MISSING],
                    display.to_screen_space((i, j))
                )


def draw_entities(surface):
    """renders entities found in entity_list"""
    for entity in entity_list:
        surface.blit(entity[0], display.to_screen_space(entity[1]))


def draw_UI(surface):
    """renders UI elements from images_to_draw on top of the tiles"""
    surface.blits(ui_images)


def render():
    """Main game render function. renders entire frame"""
    window = pygame.display.get_surface()
    window.fill("purple")
    draw_tiles(window)
    draw_entities(window)
    draw_UI(window)
    pygame.display.flip()
