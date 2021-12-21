#!/usr/bin/python3

import sys

def parse_packets(bstream, n = -1):
    bc = 0

    if n != 1:
        ps = []

        while n != 0:
            n -= 1

            try:
                ps += parse_packets(bstream[bc:], 1)
                bc += ps[-1]['size']
            except TypeError as e:
                if n >= 0:
                    raise e

                break

        return ps

    p = {}

    if bc < len(bstream):
        p['version'] = int(bstream[bc: (bc := bc + 3)], 2)

        p['type'] = int(bstream[bc: (bc := bc + 3)], 2)

        if p['type'] == 4:
            p['content'] = ''
            while(True):
                chunk = bstream[bc: (bc := bc + 5)]

                p['content'] += chunk[1:]

                if chunk[0] == '0':
                    p['content'] = int(p['content'], 2)

                    break
        else:
            bc += 1
            if bstream[bc - 1] == '0':
                size = int(bstream[bc: (bc := bc + 15)], 2)

                p['packets'] = parse_packets(bstream[bc: (bc := bc + size)])
            else:
                size = int(bstream[bc: (bc := bc + 11)], 2)

                p['packets'] = parse_packets(bstream[bc:], size)
                bc += sum([a['size'] for a in p['packets']])


        p['size'] = bc

        return [p]

def eval_packet(packet):
    try:
        return packet['content']
    except KeyError:
        pass

    if packet['type'] == 0:
        return sum([eval_packet(p) for p in packet['packets']])

    if packet['type'] == 1:
        value = 1

        for p in packet['packets']:
            value *= eval_packet(p)

        return value

    if packet['type'] == 2:
        return min([eval_packet(p) for p in packet['packets']])

    if packet['type'] == 3:
        return max([eval_packet(p) for p in packet['packets']])
 
    if packet['type'] == 5:
        return int(eval_packet(packet['packets'][0]) > eval_packet(packet['packets'][1]))

    if packet['type'] == 6:
        return int(eval_packet(packet['packets'][0]) < eval_packet(packet['packets'][1]))

    if packet['type'] == 7:
        return int(eval_packet(packet['packets'][0]) == eval_packet(packet['packets'][1]))

    raise Exception('unrecognized packet type: ' + str(packet['type']))

for stream in sys.stdin:
    packet = parse_packets(''.join([format(int(sc, 0x10), '04b') for sc in stream.strip()]), 1)

    print(eval_packet(packet[0]))