import sys
import itertools

def print_grid(grid, dim):
    for y in range(dim):
        for x in range(dim):
            sys.stdout.write('#' if (x, y) in grid else ' ')
        print
    print

def evolve_grid(grid, dim):
    new_grid = set()
    for y in range(dim):
        for x in range(dim):
            ns = set([(px, py) for px in range(x-1,x+2) for py in range(y-1, y+2)])
            ns -= set([(x,y)])

            neighbours = len(grid & ns)
            if neighbours == 3 or (neighbours == 2 and (x,y) in grid):
                new_grid.add((x,y))

    #part 2
    edges = [0, dim-1]
    corners = itertools.product(edges, edges)
    new_grid |= set(corners)

    return new_grid

def main(lines):
    dim = len(lines)

    grid = set()
    for y in range(dim):
        for x, state in list(enumerate(lines[y])):
            if state == '#':
                grid.add((x,y))


    edges = [0, dim-1]
    corners = itertools.product(edges, edges)
    grid |= set(corners)

    # for i in range(5):
    #     print "phase", i
    #     print_grid(grid, dim)
    #     grid = evolve_grid(grid, dim)


    for i in range(100):
        print i
        grid = evolve_grid(grid, dim)


    print_grid(grid,dim)
    print len(grid)





with open("day18.txt", "r") as f:
    lines = map(lambda x:x.rstrip(), f.readlines())

main(lines)