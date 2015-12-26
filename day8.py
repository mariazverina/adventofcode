import ast
def main(lines):
    #part 1
    print sum([(len(line) - len(ast.literal_eval(line))) for line in lines])
    #part 2
    print sum([(len(repr(line).replace('"','\\"')) - len(line)) for line in lines])

with open("day8.txt", "r") as f:
    lines = map(lambda x:x.rstrip(), f.readlines())

main(lines)