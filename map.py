import random
import assets

tile_map = []
SIZE = (100, 100)

dir_x = [0,  0, -1,  1]
dir_y = [1, -1,  0,  0]


def init():
    for i in range(SIZE[0]):
        tile_map.append([])
        for j in range(SIZE[1]):
            tile_map[i].append(assets.tile_textures[assets.Tiles.BLUE])
    generate()


def generate():
    current_x = int(SIZE[0] / 2)
    current_y = int(SIZE[1] / 2)

    for i in range(200):
        tmp = random.randrange(0, 4)
        current_x += dir_x[tmp]
        current_y += dir_y[tmp]
        for (x, y) in zip(dir_x, dir_y):
            tile_map[current_x + x][current_y + y] = assets.tile_textures[assets.Tiles.BROWN]
        tile_map[current_x][current_y] = assets.tile_textures[assets.Tiles.BROWN]
