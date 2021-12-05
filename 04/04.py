#!/usr/bin/python3

import sys

class Cell(int):
    def __new__(cls, val):
        obj = int.__new__(cls, val)
        obj.marked = False

        return obj

class Board():
    def __init__(self, rows):
        self.cells = rows
        self.won = False

    #returns False if board is not winning, score otherwise
    def mark(self, val):
        x_marked = [0] * len(self.cells[0])

        unmarked = 0

        y_win = False

        for x, row in enumerate(self.cells):
            y_marked = 0

            for y, cell in enumerate(row):
                if cell == val:
                    cell.marked = True

                if cell.marked:
                    y_marked += 1
                    x_marked[y] += 1
                else:
                    unmarked += cell

            if y_marked == len(row):
                y_win = True

        if y_win or len(self.cells) in x_marked:
            self.won = True

            return unmarked * val

        return False

numbers = [int(a) for a in sys.stdin.readline().split(',')]

boards = []

sys.stdin.readline()
while True:
    rows = []

    for row in sys.stdin:
        if row == "\n":
            break

        rows += [[Cell(a) for a in row.split(' ') if a != '']]

    if len(rows) > 0:
        boards += [Board(rows)]
    else:
        break

wins = []

for n in numbers:
    for board in boards:
        if board.won:
            continue

        score = board.mark(n)

        if score is not False:
            wins += [score]

if len(wins) == 0:
    raise Exception('no winning board')

print('first: ' + str(wins[0]))
print('last: ' + str(wins[-1]))
