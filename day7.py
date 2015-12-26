import re
import operator

class Gate:
    def __init__(self, var, expr, circuit):
        self.var = var
        self.expr = expr
        self.circuit = circuit
        self.val = None

    def eval(self, var):
        if var.isdigit():
            return int(var)
        return self.circuit[var].output()

    operators = {"AND":operator.and_, "OR":operator.or_, "LSHIFT":operator.lshift, "RSHIFT":operator.rshift}

    def output(self):
        global crib
        if self.val is not None:
            return self.val

        m=re.match(r"(\w+) (\w+) (\w+)", self.expr)
        if m:
            lval, op, rval = m.groups()
            lval = self.eval(lval)
            rval = self.eval(rval)
            self.val = Gate.operators[op](lval, rval)

        if self.expr.isdigit():
            self.val = int(self.expr)

        elif self.expr[:3] == "NOT":
            self.val = ~self.eval(self.expr[4:])

        if self.val is None:
            self.val =  self.eval(self.expr)

        self.val = self.val&0xffff
        return self.val

def main(lines):
    circuit = {}

    for line in lines:
        expr, var =  line.rstrip().split(" -> ")
        circuit[var] = Gate(var,expr,circuit)

    new_b = circuit['a'].output()
    for g in circuit.values():
        g.val = None

    circuit['b'].val = new_b

    print "A =", circuit['a'].output()


with open("day7.txt", "r") as f:
    lines = f.readlines()

main(lines)