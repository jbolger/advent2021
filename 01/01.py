#!/usr/bin/python3

import sys

count = 0
depths = []
depth = None

for line in sys.stdin:
    depths += [int(line)]

    if len(depths) >= 3:
        d = depths[-1] + depths[-2] + depths[-3]

        try:
            if d > depth:
                count += 1
        except TypeError:
            pass

        depth = d

        depths = depths[-3:]

print(count)
