import re

def matches((item, cnt)):
    params = {
        "children" : 3,
        "cats" : 7,
        "samoyeds" : 2,
        "pomeranians" : 3,
        "akitas" : 0,
        "vizslas" : 0,
        "goldfish" : 5,
        "trees" : 3,
        "cars" : 2,
        "perfumes" : 1
    }
    if item in "cats trees".split():
        return params[item] < cnt
    if item in "pomeranians goldfish".split():
        return params[item]  > cnt
    return params[item] == cnt

def main(lines):


    for line in lines:
        #trees: 7, vizslas: 5, akitas: 6
        m = re.match(r'Sue (\d+): (.+)',line)
        facts = m.group(2).split(", ")
        facts = map(lambda x:x.split(": "), facts)
        if all(map(matches, [(item, int(cnt)) for (item,cnt) in facts])):
            print m.groups()




with open("day16.txt", "r") as f:
    lines = map(lambda x:x.rstrip(), f.readlines())

main(lines)