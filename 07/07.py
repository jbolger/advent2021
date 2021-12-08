#!/usr/bin/python3

import sys,statistics,math

crabs = [int(crab) for crab in sys.stdin.read().split(',')]

ideal = statistics.mean(crabs)

costs = [0, 0]

def get_cost(a):
    return sum([i for i in range(1, a + 1)])

for i, target in enumerate([math.floor(ideal), math.ceil(ideal)]):
    for crab in crabs:
        costs[i] += get_cost(abs(crab - target))

print(costs[0] < costs[1] and costs[0] or costs[1])
