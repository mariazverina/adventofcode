import re
import functools

route_map = {}

def memoize(f):
    """ Memoization decorator for functions taking one or more arguments. """
    class memodict(dict):
        def __init__(self, f):
            self.f = f
        def __call__(self, *args):
            return self[args]
        def __missing__(self, key):
            ret = self[key] = self.f(*key)
            return ret
    return memodict(f)


@memoize
def min_path(origin, cities):
    global route_map
    if len(cities) == 0:
        return (0, [])
    ml = 999999
    mp = []
    for c in cities:
        l, p = min_path(c, cities.difference(set([c])))
        l += route_map[(origin, c)]
        if l < ml:
            mp = [c] + p
            ml = l
    return ml, mp

def max_path(origin, cities):
    global route_map
    if len(cities) == 0:
        return (0, [])
    ml = 0
    mp = []
    for c in cities:
        l, p = max_path(c, cities.difference(set([c])))
        l += route_map[(origin, c)]
        if l > ml:
            mp = [c] + p
            ml = l
    return ml, mp

def main(lines):
    global route_map
    cities = set()
    for line in lines:
        src, dst, dist = re.match(r'(\w+) to (\w+) = (\d+)', line).groups()
        route_map[(src,dst)] = route_map[(dst,src)] = int(dist)
        cities.add(src)
        cities.add(dst)

    for c in cities:
        route_map[("origin", c)] = 0

    print min_path('origin', frozenset(cities))
    print max_path('origin', frozenset(cities))

with open("day9.txt", "r") as f:
    lines = map(lambda x:x.rstrip(), f.readlines())

