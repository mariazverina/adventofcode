import re
import operator

def product(seq):
    return reduce(operator.mul,seq,1)

def max_score(ingredients, volume, mix, recipe):
    if len(ingredients) == 0:
        # print mix
        if mix[-1] != 500 or len([1 for m in mix if m <= 0]) > 0:
            return 0, []
        # if recipe == [24, 29, 31, 16]:
        #     print "winning mix score", mix
        return product(mix[:-1]), []

    max_result = 0
    max_list = []

    for i in range(0,volume+1):
        a_score, a_list = max_score(ingredients[1:],volume-i, mix, recipe + [i])
        if a_score > max_result:
            max_result = a_score
            max_list = a_list
            max_list.insert(0,i)
        mix = map(sum, zip(mix, ingredients[0]))

    return max_result, max_list



def main(lines):
    params = []

    for line in lines:
        m = re.match(r'(\w+): capacity (-?\d+), durability (-?\d+), flavor (-?\d+), texture (-?\d+), calories (\d+)',line)
        # name = m.group(1)
        params.append(map(int, m.groups()[1:]))

    print params
    print max_score(params,100,[0]*5,[])



with open("day15.txt", "r") as f:
    lines = map(lambda x:x.rstrip(), f.readlines())

main(lines)