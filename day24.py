fcache = {}



def find_first_sum(packages, target, used, max_packages=99):
    if target < 0:
        return None
    if len(used) > max_packages:
        return None
    if target == 0:
        return []

    global fcache
    cache_key = (frozenset([p for p in used if p <= target]), target, max_packages)
    if cache_key in fcache:
        return fcache[cache_key]

    for p in packages:
        if p in used or p > target:
            continue
        used.add(p)
        solution = find_first_sum(packages, target - p, used, max_packages)
        if solution is not None:
            solution = [p] + solution
            fcache[cache_key] = solution
            return solution
        used.remove(p)

    if len(fcache) % 10000 == 0:
        print len(fcache)

    fcache[cache_key] = None
    return None

mcache = {}

def find_min_sum(packages, target, used, max_packages):
    if target < 0 or len(used) > max_packages:
        return 99999, None
    if target == 0:
        return 1, []

    global mcache
    cache_key = (frozenset([p for p in used if p <= target]), target, max_packages)
    if cache_key in mcache:
        return mcache[cache_key]

    minsol = (1e99, [])
    for p in packages:
        if p in used or p > target:
            continue
        used.add(p)
        entaglement, solution = find_min_sum(packages, target - p, used, max_packages)
        if solution is not None:
            solution = entaglement * p, [p] + solution
            if solution < minsol:
                minsol = solution
        used.remove(p)

    if len(mcache) % 10000 == 0:
        print "m", len(mcache)

    if minsol == (1e99, []):
        minsol == None

    mcache[cache_key] = minsol
    return minsol


def main(program):
    packages = map(int, lines)

    total_weight = sum(packages)
    print len(packages)

    packages = sorted(packages, reverse=True) # greedy


    # initialize to a greedy solution
    comp1 = find_first_sum(packages, total_weight / 3, set(), 6)
    print comp1 # this explain why can get away with 6 deep
    comp2 = find_first_sum(packages, total_weight / 3, set(comp1))

    passenger_count = len(comp1)

    print find_min_sum(packages, total_weight / 4, set(), 6)

    # while comp1 is not None:
    #
    # while find_sum(packages, target, set(), passenger_count - 1) is not None:
    #
    #     passenger_count -= 1
    #     print "Found solution with {0} packages in passenger compartment".format(passenger_count)
    #     print find_sum(packages, target, set(), passenger_count - 1)



    print comp1, comp2



with open("day24.txt", "r") as f:
    lines = map(lambda x:x.rstrip(), f.readlines())

main(lines)