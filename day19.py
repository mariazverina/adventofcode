import re
import itertools

substitutions = []
def replace(parts, what, alternative):
    if len(parts) < 2:
        return parts

    me = [parts[0] + alternative + what.join(parts[1:])]
    combos = replace(parts[1:], what, alternative)
    combos = [parts[0] + what + c for c in combos]
    combos = me + combos
    return combos

def all_subs(molecule, reverse=False):
    global substitutions
    substituted_molecules = set()
    for what, alt in substitutions:
        if reverse:
            what, alt = alt, what
        candidates = replace(molecule.split(what), what, alt)
        # print qq, what, alt
        substituted_molecules |= set(candidates)
    substituted_molecules -= set([molecule])
    return sorted(substituted_molecules, key=len)

def mutate_list_backwards(molecules):
    return itertools.chain.from_iterable( map(lambda x:all_subs(x,True), molecules))


def main(lines):
    line = lines.pop(0)
    global substitutions
    while len(line) > 0:
        m = re.match('(\w+) => (\w+)', line)
        substitutions.append(m.groups())
        line = lines.pop(0)

    molecule = lines.pop(0)
    print len(molecule)

    mutated = [molecule]
    for i in range(210):
        print i, mutated
        mutated = sorted(set(mutate_list_backwards(mutated)), key=len)[:12] # guess the pruning electron comes out
    print len(mutated)

with open("day19.txt", "r") as f:
    lines = map(lambda x:x.rstrip(), f.readlines())

main(lines)