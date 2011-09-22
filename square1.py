from itertools import count, product
import sys


def T(piece):
    return {
        1: 1,
        2: 2,
        3: 6,
        4: 3,
        5: 4,
        6: 5,
        7: 7,
        8: 8,
        10: 10,
        20: 30,
        30: 60,
        40: 40,
        50: 20,
        60: 50,
        70: 70,
        80: 80,
    }[piece]

def B(piece):
    return {
        1: 8,
        2: 1,
        3: 3,
        4: 4,
        5: 5,
        6: 6,
        7: 2,
        8: 7,
        10: 40,
        20: 20,
        30: 30,
        40: 70,
        50: 50,
        60: 60,
        70: 80,
        80: 10,
    }[piece]

def t(piece):
    return {
        1: 2,
        2: 4,
        3: 1,
        4: 3,
        5: 5,
        6: 6,
        7: 7,
        8: 8,
        10: 20,
        20: 30,
        30: 40,
        40: 10,
        50: 50,
        60: 60,
        70: 70,
        80: 80,
    }[piece]

def b(piece):
    return {
        1: 1,
        2: 2,
        3: 3,
        4: 4,
        5: 6,
        6: 8,
        7: 5,
        8: 7,
        10: 10,
        20: 20,
        30: 30,
        40: 40,
        50: 60,
        60: 70,
        70: 80,
        80: 50,
    }[piece]

def a(piece):
    return {
        1: 4,
        2: 1,
        3: 3,
        4: 2,
        5: 7,
        6: 5,
        7: 6,
        8: 8,
        10: 40,
        20: 20,
        30: 10,
        40: 30,
        50: 80,
        60: 50,
        70: 70,
        80: 60,
    }[piece]

def c(piece):
    return {
        1: 4,
        2: 3,
        3: 1,
        4: 2,
        5: 7,
        6: 6,
        7: 5,
        8: 8,
        10: 40,
        20: 20,
        30: 10,
        40: 30,
        50: 80,
        60: 50,
        70: 70,
        80: 60,
    }[piece]

def s(piece):
    return {
        1: 7,
        2: 5,
        3: 1,
        4: 8,
        5: 6,
        6: 2,
        7: 3,
        8: 4,
        10: 40,
        20: 20,
        30: 20,
        40: 10,
        50: 60,
        60: 50,
        70: 80,
        80: 70,
    }[piece]


def sequences():
    transformations = [T, B, t, b, a, c, s]

    for moves in count(1):
        print moves
        for p in product(*([transformations] * moves)):
            yield p


needed = dict(map(int, item.split(':')) for item in sys.argv[1:])


for sequence in sequences():
    for piece, position in needed.iteritems():
        result = reduce(lambda piece, t: t(piece), [piece] + list(sequence))

        if result != position:
            break
    else:
        print [func.__name__ for func in sequence]
        break
