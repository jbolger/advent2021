#!/usr/bin/python3

import sys

bits = {}

for i, bit in enumerate('abcdefg'):
    bits[bit] = 1 << i

total = 0

for row in sys.stdin:
    [numerals, output] =  [a.split(' ') for a in row.strip("\n").split(' | ')]

    [_zero, _one, _two, _three, _four, _five, _six, _seven, _eight, _nine] = [0] * 10
    [_b, _c, _d, _f] = [0] * 4

    len_map = [[] for i in range(0,8)]

    for i, numeral in enumerate(numerals):
        numerals[i] = 0

        for bit in numeral:
            numerals[i] |= bits[bit]

        len_map[len(numeral)] += [numerals[i]]

    for i, numeral in enumerate(output):
        output[i] = 0

        for bit in numeral:
            output[i] |= bits[bit]

    output.reverse()

    _eight = 0b1111111

    _one = len_map[2][0]
    _c = _one
    _f = _one

    _seven = len_map[3][0]

    _four = len_map[4][0]
    _b = _four ^ _one
    _d = _b

    for numeral in len_map[6]:
        if _b == _d and numeral & _d != _d:
            _zero = numeral
            _b &= _zero
            _d ^= _b

            continue

        if _c == _f and numeral & _c != _c:
            _six = numeral
            _f &= _six
            _c ^= _f

            continue

        _nine = numeral

    for numeral in len_map[5]:
        if not numeral & _f:
            _two = numeral

            continue

        if not numeral & _c:
            _five = numeral

            continue

        _three = numeral

    value_map = {}

    for value, numeral in enumerate([_zero, _one, _two, _three, _four, _five, _six, _seven, _eight, _nine]):
        value_map[numeral] = value

    number = 0

    for i, numeral in enumerate(output):
        number += value_map[numeral] * (10 ** i)

    total += number

print(total)
