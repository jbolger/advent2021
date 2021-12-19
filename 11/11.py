#!/usr/bin/python3

import sys

grid = {}

i = -1
for row in sys.stdin:
    i += 1
    grid[i] = {i : int(v) for i, v in enumerate(row.strip("\n"))}

total_flashes = 0

generations = 0
while True:
    generations += 1

    for i in grid:
        for j in grid:
            grid[i][j] += 1

    popped = True

    flashes = 0

    while popped:
        popped = False

        cells = 0

        for i in grid:
            for j in grid[i]:
                cells += 1

                if grid[i][j] > 9:
                    popped = True

                    for ii in range(-1, 2):
                        for jj in range(-1, 2):
                            try:
                                if grid[i + ii][j + jj]:
                                    grid[i + ii][j + jj] += 1
                            except KeyError:
                                pass

                    grid[i][j] = 0

                    flashes += 1

    total_flashes += flashes

    if flashes == cells:
        print('synch: ' + str(generations))

        break

print('flashes: ' + str(total_flashes))
