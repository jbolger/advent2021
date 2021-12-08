#!/usr/bin/python3

import sys

lines = []
grid = {}

for line in sys.stdin:
    line = line.split(' -> ')

    for i, coords in enumerate(line):
        coords = coords.split(',')
        line[i] = [int(a) for a in coords]

    if line[0][0] == line[1][0]:
        for i in line[0][1] <= line[1][1] and range(line[0][1], line[1][1] + 1) or range(line[1][1], line[0][1] + 1):
            try:
                grid['%dx%d' % (line[0][0], i)] += 1
            except KeyError:
                grid['%dx%d' % (line[0][0], i)] = 1
    elif line[0][1] == line[1][1]:
        for i in line[0][0] <= line[1][0] and range(line[0][0], line[1][0] + 1) or range(line[1][0], line[0][0] + 1):
            try:
                grid['%dx%d' % (i, line[0][1])] += 1
            except KeyError:
                grid['%dx%d' % (i, line[0][1])] = 1
    else:
        x_inc = 1
        y_inc = 1
        y_start = line[0][1]

        if line[0][0] < line[1][0]:
            if line[0][1] > line[1][1]:
                y_inc = -1
        elif line[0][0] > line[1][0]:
            x_inc = -1
            y_start = line[1][1]

            if line[1][1] > line[0][1]:
                y_inc = -1

        j = -1
        for i in x_inc > 0 and range(line[0][0], line[1][0] + 1) or range(line[1][0], line[0][0] + 1):
            j += 1

            try:
                grid['%dx%d' % (i, y_start + (j * y_inc))] += 1
            except KeyError:
                grid['%dx%d' % (i, y_start + (j * y_inc))] = 1

print(sum([1 for a in grid if grid[a] > 1]))
