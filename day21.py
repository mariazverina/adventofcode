from collections import namedtuple
import itertools
import operator
import math

weapons = """Dagger        8     4       0
Shortsword   10     5       0
Warhammer    25     6       0
Longsword    40     7       0
Greataxe     74     8       0"""

armours = """Leather      13     0       1
Chainmail    31     0       2
Splintmail   53     0       3
Bandedmail   75     0       4
Platemail   102     0       5"""

rings = """Damage+1    25     1       0
Damage+2    50     2       0
Damage+3   100     3       0
Defense+1   20     0       1
Defense+2   40     0       2
Defense+3   80     0       3"""


def convert(sl):
    sl = sl.split()
    sl = [int(a) if a.isdigit() else a for a in sl]
    tuples = zip(*([iter(sl)] * 4))
    return map(lambda x: Item(*x), tuples)


def combos(items, count, allow_none=True):
    combos = reduce(operator.add, map(list, [itertools.combinations(items, i) for i in range(1, count + 1)]))
    if allow_none:
        combos += [(Item("None", 0, 0, 0),)]
    return combos



def eval_combo(combo):
    return map(lambda x: reduce(operator.add, x), zip(*combo))


# Hit Points: 109
# Damage: 8
# Armor: 2
def winning_combo(combo):
    boss_dmg = 8
    boss_arm = 2
    _, cost, dmg, arm = combo
    boss_rounds = math.ceil(109.0 / max(1, dmg-boss_arm))
    my_rounds   = math.ceil(100.0 / max(1, boss_dmg-arm))
    return my_rounds >= boss_rounds




Item = namedtuple("Item", "name cost damage armour")

weapons = convert(weapons)
armours = convert(armours)
rings = convert(rings)

w_combos = combos(weapons, 1, allow_none=False)
a_combos = combos(armours, 1)
r_combos = combos(rings, 2)

all_combos = [Item(*eval_combo(w+a+r)) for w in w_combos for a in a_combos for r in r_combos]

win_combos = [c for c in all_combos if winning_combo(c)]
lose_combos = [c for c in all_combos if not winning_combo(c)]

print sorted(win_combos, key=lambda x:x[1])
print sorted(lose_combos, key=lambda x:x[1], reverse=True)