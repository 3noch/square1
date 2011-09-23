from itertools import count, product
import sys


def transformation(name, d):
    expected = set(range(1, 9) + range(10, 90, 10))

    if set(d.iterkeys()) - expected or set(d.itervalues()) - expected:
        raise ValueError('invalid transformation for ' + name)

    _transformation = lambda piece: d[piece]
    _transformation.__name__ = name
    return _transformation


T = transformation('T', {
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
})

B = transformation('B', {
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
})

t = transformation('t', {
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
})

b = transformation('b', {
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
})

a = transformation('a', {
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
})

c = transformation('c', {
    1: 4,
    2: 3,
    3: 1,
    4: 2,
    5: 7,
    6: 6,
    7: 5,
    8: 8,
    10: 30,
    20: 40,
    30: 20,
    40: 10,
    50: 50,
    60: 70,
    70: 60,
    80: 80,
})

s = transformation('s', {
    1: 7,
    2: 5,
    3: 1,
    4: 8,
    5: 6,
    6: 2,
    7: 3,
    8: 4,
    10: 40,
    20: 30,
    30: 20,
    40: 10,
    50: 60,
    60: 50,
    70: 80,
    80: 70,
})

cbcbc = transformation('c b c b^-1 c', {
    1: 3,
    2: 4,
    3: 2,
    4: 1,
    5: 8,
    6: 6,
    7: 7,
    8: 5,
    10: 40,
    20: 30,
    30: 10,
    40: 20,
    50: 70,
    60: 60,
    70: 50,
    80: 80,
})

TB = transformation('T^2 B^2', {
    1: 7,
    2: 8,
    3: 5,
    4: 6,
    5: 3,
    6: 4,
    7: 1,
    8: 2,
    10: 70,
    20: 60,
    30: 50,
    40: 80,
    50: 30,
    60: 20,
    70: 10,
    80: 40,
})


def sequences():
    transformations = [T, B, t, b, a, c, s, cbcbc, TB]

    for moves in count(1):
        print moves
        for p in product(*([transformations] * moves)):
            yield p


needed = dict(map(int, item.split(':')) for item in sys.argv[1:])


for sequence in sequences():
    for piece in needed:
        new_position = piece

        for step in sequence:
            new_position = step(new_position)

        if new_position != needed[piece]:
            break
    else:
        print [func.__name__ for func in sequence]
        break
