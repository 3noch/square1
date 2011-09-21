from itertools import count, product
import sys


def transformation(*pieces):
    return {i + 1: val for i, val in enumerate(pieces)}


transformations = {
    'T': transformation(1, 2, 6, 3, 4, 5, 7, 8, 9, 11, 14, 12, 10, 13, 15, 16),
    'B': transformation(8, 1, 3, 4, 5, 6, 2, 7, 12, 10, 11, 15, 13, 14, 16, 9),
    't': transformation(2, 4, 1, 3, 5, 6, 7, 8, 10, 11, 12, 9, 13, 14, 15, 16),
    'b': transformation(1, 2, 3, 4, 6, 8, 5, 7, 9, 10, 11, 12, 14, 15, 16, 13),
    'a': transformation(4, 1, 3, 2, 7, 5, 6, 8, 12, 10, 9, 11, 16, 13, 15, 14),
    'c': transformation(4, 3, 1, 2, 7, 6, 5, 8, 11, 12, 10, 9, 13, 15, 14, 16),
    's': transformation(7, 5, 1, 4, 6, 2, 3, 4, 12, 11, 10, 9, 14, 13, 16, 15),
    'c b c b^-1 c': transformation(3, 4, 2, 1, 8, 6, 7, 5, 12, 11, 9, 10, 15, 14, 13, 16),
    'T^2 B^2': transformation(7, 8, 5, 6, 3, 4, 1, 2, 15, 14, 13, 16, 11, 10, 9, 12),
}

base = {i: i for i in range(1, 17)}


def transform(transformation_matrix, original):
    return {key: transformation_matrix.get(val, val)
            for key, val in original.iteritems()}


def chain(matrix, *transformations):
    for t in transformations:
        matrix = transform(t, matrix)

    return matrix


def test(real, required):
    for key, val in required.iteritems():
        if real[key] != val:
            return False

    return True


def try_moves(moves, needed):
    for p in product(*([transformations.values()] * moves)):
        if test(chain(base, *p), needed):
            return p


def give_name(t):
    for name, transformation in transformations.iteritems():
        if t == transformation:
            return name


def tell_moves(moves, needed):
    transformations = try_moves(moves, needed)

    if transformations:
        return ' '.join(give_name(t) for t in transformations)


needed = dict(map(int, item.split(':')) for item in sys.argv[1:])

for i in count(1):
    result = tell_moves(i, needed)

    if result:
        print result
        break
