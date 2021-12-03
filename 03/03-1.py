#!/usr/bin/python3

import sys

sums = []

half = 0

for line in sys.stdin:
    half += .5

    for i, v in enumerate(line):
        if v == '1':
            try:
                sums[i] += 1
            except IndexError:
                sums += [1]
        elif v in ['0', '\n']:
            pass
        else:
            raise Exception('unrecognized input')

gamma = 0
epsilon = 0

for i, v in enumerate(sums):
    if v > half:
        gamma |= 1 << (len(sums) - i - 1)
    elif v < half:
        epsilon |= 1 << (len(sums) -i - 1)
    else:
        raise Exception('ambiguous input')

print(gamma * epsilon)
