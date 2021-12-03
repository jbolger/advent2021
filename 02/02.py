#!/usr/bin/python3

import sys

x = 0
y = 0
angle = 0

for line in sys.stdin:
    direction = line[0:line.index(' ')]
    magnitude = int(line[line.index(' ') + 1:])

    if direction == 'forward':
        x += magnitude
        y += magnitude * angle

        if y < 0:
            y = 0
    elif direction == 'up':
        angle -= magnitude
    elif direction == 'down':
        angle += magnitude
    else:
        raise Exception('unrecognized direction')

print(x * y)
