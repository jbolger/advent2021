#!/usr/bin/python3

import sys

class ParseInvalidChar(Exception):
    pass

class ParseUnrecognizedChar(Exception):
    pass

class ParseIncompleteCmd(Exception):
    pass

def Parse(cmd):
    gc = [None]

    g = {
        '(' : ')',
        '[' : ']',
        '{' : '}',
        '<' : '>',
        None : "\n"
    }

    for c in cmd.strip():
        error = True

        for k in g:
            if c == k:
                gc += [c]

                error = False

                break

            if c == g[k]:
                if gc[-1] == k:
                    gc.pop()

                    error = False

                    break
                else:
                    raise ParseInvalidChar(c)

        if error:
            raise ParseUnrecognizedChar(c)

    if gc != [None]:
        gc.reverse()
        gc.pop()

        raise ParseIncompleteCmd(''.join(gc))

score_p1 = 0

scores_p2 = []

line = 0

for cmd in sys.stdin:
    line += 1

    try:
        Parse(cmd)
    except ParseInvalidChar as e:
        score = e.args[0] == ')' and 3 or e.args[0] == ']' and 57 or e.args[0] == '}' and 1197 or e.args[0] == '>' and 25137 or 0

        score_p1 += score

        #print(str(line) + ': ' + str(e) + ': ' + cmd.strip() + ': (' + str(score) +')')
    except ParseIncompleteCmd as e:
        score = 0

        for c in e.args[0]:
            score *= 5
            score += c == '(' and 1 or c == '[' and 2 or c == '{' and 3 or c == '<' and 4 or 0

        scores_p2 += [score]

        #print(str(line) + ': ' + str(e) + ': ' + cmd.strip() + ': (' + str(score) + ')')

import statistics 

print('score p1: ' + str(score_p1))
print('score p2: ' + str(statistics.median(scores_p2)))
