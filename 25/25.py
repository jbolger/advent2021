#!/usr/bin/python3

import sys

grid = {}

w = 0
h = 0

def get(i, j):
    return 'x'.join([str(i % h), str(j % w)])

for i, line in enumerate(sys.stdin):
    h += 1
    w = 0
    for j, c in enumerate(line.strip()):
        w += 1

        if c != '.':
            grid[str(i) + 'x' + str(j)] = c

t = 0
while t := t + 1:
    move = False

    for ew in [['>', 0, 1], ['v', 1, 0]]:
        _grid = {}

        for k in grid:
            v = grid[k]
            [i, j] = [int(a) for a in k.split('x')]

            if v == ew[0]:
                if not grid.get(get(i + ew[1], j + ew[2])):
                    _grid[get(i, j)] = False
                    _grid[get(i + ew[1], j + ew[2])] = ew[0]
                    move = True

        for k in _grid:
            if _grid[k]:
                grid[k] = _grid[k]
            else:
                del(grid[k])

    if not move:
        break

print(t)

