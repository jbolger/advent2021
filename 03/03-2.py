#!/usr/bin/python3

import sys

values = []

matches = []

for line in sys.stdin:
    values += [line]

for h, vals in enumerate([values, values]):
    i = -1
    while len(vals) > 1:
        i += 1

        _vals = []

        count = 0
        count_all = 0

        for val in vals:
            count_all += 1

            if val[i] == '1':
                count += 1

        keep = h and str(int(count >= count_all / 2)) or str(int(not count >= count_all / 2))

        for val in vals:
            if val[i] == keep:
                _vals += [val]

        vals = _vals

    matches += [int(vals[0], 2)]

    if matches[-1] == 0:
        break

print(matches[0] * matches[1])
