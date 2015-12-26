from collections import Counter

def main(lines):
    containers = map(int, lines)
    print len(containers), containers

    n_sol = 0
    c_per_sol = []

    for i in range(2**len(containers)):
        cap = sum([(i>>j & 1) * size for (j,size) in enumerate(containers)])
        if cap == 150:
            n_sol += 1
            n_c = sum([i >> j & 1 for j in range(len(containers))])
            c_per_sol.append(n_c)

    print n_sol
    print Counter(c_per_sol)





with open("day17.txt", "r") as f:
    lines = map(lambda x:x.rstrip(), f.readlines())

main(lines)