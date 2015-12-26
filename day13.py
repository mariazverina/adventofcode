import re
import itertools

def main(lines):
    people = set()
    table = {}

    for line in lines:
        m = re.match(r'(\w+) would (\w+) (\d+) happiness units by sitting next to (\w+).', line)

        a, ve, amt, b =  m.groups()
        people.add(a)
        ve = -1 if ve == "lose" else 1
        amt = int(amt) * ve
        table[(a,b)] = amt

    print people
    print table

    for p in people:
        table[('me',p)] = 0
        table[(p,'me')] = 0

    people.add('me')

    perms = itertools.permutations(sorted(people))

    mv = 0
    ml = []
    for tl in perms:
        tv = 0
        for i in range(len(tl)):
            a = tl[i]
            b = tl[i-1]
            tv += table[(a,b)]+table[(b,a)]
        if tv > mv:
            mv = tv
            ml = tl

    print mv, ml



with open("day13.txt", "r") as f:
    lines = map(lambda x:x.rstrip(), f.readlines())

main(lines)