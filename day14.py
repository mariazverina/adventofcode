import re
from itertools import chain
from collections import Counter


class Reindeer():
    def __init__(self, name, velocity, sprint_duration, rest_duration):
        self.name = name
        self.velocity = velocity
        self.sprint_duration = sprint_duration
        self.rest_duration = rest_duration

    def cycle_time(self):
        return self.sprint_duration + self.rest_duration

    def distance(self, seconds):
        n_cycles = seconds / self.cycle_time()
        remainder = seconds % self.cycle_time()

        return (n_cycles * self.sprint_duration + min(remainder, self.sprint_duration)) * self.velocity


def race(reindeer, distance):
    return sorted(map(lambda x: (x.distance(distance), x.name), reindeer), reverse=True)

def winners(race):
    return [name for (dist, name) in race if dist==race[0][0]]


def main(lines):
    reindeer = []

    for line in lines:
        m = re.match(r'(\w+) can fly (\d+) km/s for (\d+) seconds, but then must rest for (\d+) seconds.',line)
        name = m.group(1)
        velocity, sprint_duration, rest_duration = map(int, m.groups()[1:])
        reindeer.append(Reindeer(name,velocity,sprint_duration,rest_duration))


    distance=2503
    # distance=1000


    r = race(reindeer, distance)

    print r
    print winners(r)

    points_winners = map(winners, map(lambda dist:race(reindeer, dist), range(1,distance+1)))
    print points_winners

    print Counter(chain(*points_winners))




with open("day14.txt", "r") as f:
    lines = map(lambda x:x.rstrip(), f.readlines())

main(lines)