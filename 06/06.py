#!/usr/bin/python3

import sys

class School():
    def __init__(self, fishes):
        self.ages = [0] * 9

        for fish in fishes:
            self.ages[fish] += 1

    def next(self):
        _ages = [0] * 9

        for age, total in enumerate(self.ages[1:]):
            _ages[age] = total

        _ages[8] += self.ages[0]
        _ages[6] += self.ages[0]

        self.ages = _ages

    def total(self):
        return sum(self.ages)

school = School([int(fish) for fish in sys.stdin.read().split(',')])

for i in range(0, 256):
    school.next()

print(school.total())
