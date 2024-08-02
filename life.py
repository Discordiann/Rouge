moore_dir = [(-1, 1),  (0, 1),  (1, 1),
             (-1, 0),           (1, 0),
             (-1, -1), (0, -1), (1, -1)]
conway_life = (set([3]), set([2, 3]))


blinker = [[0, 0, 0, 0, 0],
           [0, 0, 1, 0, 0],
           [0, 0, 1, 0, 0],
           [0, 0, 1, 0, 0],
           [0, 0, 0, 0, 0]]


def celular_automata(ruleset: (set, set), start, steps):
    """ruleset is the birth set, followed by the survival set"""
    size_x = len(start)
    size_y = len(start[0])
    prev = []
    for x in range(size_x):
        prev.append([])
        for y in range(size_y):
            prev[x].append(start[x][y])
    next = []
    for x in range(size_x):
        next.append([0]*size_y)
    for i in range(steps):
        for x in range(size_x):
            t_arr = []
            for y in range(size_y):
                temp = 0
                for (x_off, y_off) in moore_dir:
                    nx = (x_off + x) % size_x
                    ny = (y_off + y) % size_y
                    temp += start[nx][ny]
                t_arr.append(temp)
                if temp in ruleset[start[x][y]]:
                    next[x][y] = 1
                else:
                    next[x][y] = 0
        temp = prev
        prev = next
        next = prev
    return next
