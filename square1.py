from itertools import count, product
import sys


transformations = {
    'T': {3:6, 6:5, 5:4, 4:3, 20:30, 30:60, 60:50, 50:20},
    'B': {1:8, 8:7, 7:2, 2:1, 10:40, 40:70, 70:80, 80:10},
    't': {1:2, 2:4, 4:3, 3:1, 10:20, 20:30, 30:40, 40:10},
    'b': {5:6, 6:8, 8:7, 7:5, 50:60, 60:70, 70:80, 80:50},
    'a': {1:4, 4:2, 2:1, 5:7, 7:6, 6:5, 10:40, 40:30, 30:10, 50:80, 80:60, 60:50},
    'c': {1:4, 4:2, 2:3, 3:1, 5:7, 7:5, 10:30, 30:20, 20:40, 40:10, 60:70, 70:60},
    's': {1:7, 7:3, 3:1, 2:5, 5:6, 6:2, 4:8, 8:4, 10:40, 40:10, 20:30, 30:20, 50:60, 60:50, 70:80, 80:70},
    'c b c b^-1 c': {1:3, 3:2, 2:4, 4:1, 5:8, 8:5, 10:40, 40:20, 20:30, 30:10, 50:70, 70:50},
    'T^2 B^2': {1:7, 7:1, 2:8, 8:2, 3:5, 5:3, 4:6, 6:4, 10:70, 70:10, 20:60, 60:20, 30:50, 50:30, 40:80, 80:40},
}

names = range(1, 9) + [10 * i for i in xrange(1, 9)]
base = {i: i for i in names}


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
