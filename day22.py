# Magic Missile costs 53 mana. It instantly does 4 damage.
# Drain costs 73 mana. It instantly does 2 damage and heals you for 2 hit points.
# Shield costs 113 mana. It starts an effect that lasts for 6 turns. While it is active, your armor is increased by 7.
# Poison costs 173 mana. It starts an effect that lasts for 6 turns. At the start of each turn while it is active, it deals the boss 3 damage.
# Recharge costs 229 mana. It starts an effect that lasts for 5 turns. At the start of each turn while it is active, it gives you 101 new mana.

import copy

class Game:
    SHIELD_ARMOUR = 7
    POISON_DAMAGE = 3
    RECHARGE_MANA = 101
    spells = []

    def __init__(self, me_mana=500, me_hp=50, boss_hp=51, boss_dmg=9):
        self.me_mana  = me_mana
        self.me_hp = me_hp
        self.boss_hp = boss_hp
        self.boss_dmg = boss_dmg
        self.me_armour = 0
        self.buffs = []
        self.finished_buffs = []
        self.my_turn = True
        self.history = []

    def summary(self, armour):
        pass
        print "-- {0} Turn".format("Player" if self.my_turn else "Boss")
        print self
        for b in self.buffs:
            print "{0} has {1} turns left".format(b.spell_name(), b.duration)

    def do_buffs(self):
        for b in self.buffs:
            b.do_buff(self)
            b.duration -= 1

        self.finished_buffs = [b for b in self.buffs if b.duration <= 0]
        self.buffs = [b for b in self.buffs if b.duration > 0]

    def post_turn(self):
        [b.buff_finished(self) for b in self.finished_buffs]

    def turn(self, spell):
        if self.my_turn:
            self.me_hp -= 1
            if self.me_hp <= 0:
                return

        self.do_buffs()
        # self.summary(0)
        if self.my_turn:
            # if any([spell.spell_name() == b.spell_name() for b in self.buffs]):
            #     self.me_hp = -1
            spell.action(self)
            if self.me_mana < 0:
                self.me_hp = -1
                return
            self.history.append(spell)
        else:
            dmg = max(1, self.boss_dmg - self.me_armour)
            if self.boss_hp > 0:
                self.me_hp -= dmg

        self.post_turn()
        self.my_turn = not self.my_turn


    def game_finished(self):
        return self.me_hp <= 0 or self.boss_hp <= 0

    def game_won(self):
        return self.game_finished() and self.me_hp > 0

    def __repr__(self):
        buffs = [b.spell_name() + ":" + str(b.duration) for b in self.buffs]
        return "Game: Me({me_hp}, {me_mana}). Boss ({boss_hp}). Buffs: {0}".format(','.join(buffs),**self.__dict__)

class Spell:
    def __init__(self, cost, duration):
        self.cost = cost
        self.duration = duration

    def action(self, game):
        game.me_mana -= self.cost

    def spell_name(self):
        return "Base Spell"

    def do_buff(self, game):
        pass

    def buff_finished(self, game):
        pass


class Missile(Spell):
    def __init__(self):
        Spell.__init__(self, 53, 0)

    def spell_name(self):
        return "Missile"

    def action(self, game):
        # print "You fire missile at boss"
        Spell.action(self, game)
        game.boss_hp -= 4

class Drain(Spell):
    def __init__(self):
        Spell.__init__(self, 73, 0)

    def spell_name(self):
        return "Drain"

    def action(self, game):
        # print "You drain the boss"
        Spell.action(self, game)
        game.boss_hp -= 2
        game.me_hp += 2


class Shield(Spell):
    def __init__(self):
        Spell.__init__(self, 113, 6)

    def spell_name(self):
        return "Shield"

    def action(self, game):
        # print "You cast a shield"
        Spell.action(self, game)
        game.buffs.append(self)

    def do_buff(self, game):
        game.me_armour = Game.SHIELD_ARMOUR

    def buff_finished(self, game):
        game.me_armour = 0

class Poison(Spell):
    def __init__(self):
        Spell.__init__(self, 173, 6)

    def spell_name(self):
        return "Poison"

    def action(self, game):
        # print "You cast a poison"
        Spell.action(self, game)
        game.buffs.append(self)

    def do_buff(self, game):
        game.boss_hp -= Game.POISON_DAMAGE

class Recharge(Spell):
    def __init__(self):
        Spell.__init__(self, 229, 5)

    def spell_name(self):
        return "Recharge"

    def action(self, game):
        # print "You cast a recharge"

        Spell.action(self, game)
        game.buffs.append(self)

    def do_buff(self, game):
        game.me_mana += Game.RECHARGE_MANA

fcache = {}

def min_cost(game, cost_so_far, best_solution):
    global fcache
    if game.me_mana < 0 or best_solution <= 0:
        return 9999, []

    if game.game_finished():
        if game.game_won():
            print "Solution found with end: ", game
            print cost_so_far, [s.spell_name() for s in game.history]
            return (0, [])
        else:
            return (9999, [])

    if game.my_turn:
        minc = 9999
        minl = []
        for s in Game.spells:
            s = s()
            if any([s.spell_name() == b.spell_name() for b in game.buffs if b.duration > 1]):
                continue
            cache_key = repr(game)
            if cache_key in cache:
                return cache[cache_key]
            g = copy.deepcopy(game)
            g.turn(s)
            c, ml = min_cost(g, cost_so_far + s.cost, min(minc, best_solution) - s.cost)
            c += s.cost

            if c < minc:
                minc = c
                minl = [s.spell_name()] + ml


        cache[cache_key] = minc, minl
        return minc, minl

    else:
        game.turn(None)
        return min_cost(game, cost_so_far, best_solution)

Game.spells = [Missile, Drain, Shield, Poison, Recharge]

g = Game()
cost, seq = min_cost(g, 0, 9999)
print cost, seq
