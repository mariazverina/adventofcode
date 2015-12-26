from collections import namedtuple

# hlf r sets register r to half its current value, then continues with the next instruction.
# tpl r sets register r to triple its current value, then continues with the next instruction.
# inc r increments register r, adding 1 to it, then continues with the next instruction.
# jmp offset is a jump; it continues with the instruction offset away relative to itself.
# jie r, offset is like jmp, but only jumps if register r is even ("jump if even").
# jio r, offset is like jmp, but only jumps if register r is 1 ("jump if one", not odd).

Registers = namedtuple("Registers", "a b pc")
class Registers:
    def __init__(self):
        self.a = 0
        self.b = 0
        self.pc = 0

    def get_register(self, name):
        return self.__dict__[name]

    def set_register(self, name, val):
        self.__dict__[name] = val

    def jmp(self, offset):
        self.pc += int(offset) - 1 # pc is auto-incremented by 1, hence undo this for jumps

    def __repr__(self):
        return "a:{a} b:{b} pc:{pc}".format(**self.__dict__)


def apply_f_to_reg(regs, params, f):
    r, = params
    regs.set_register(r, f(regs.get_register(r)))


def inc(regs, params):
    apply_f_to_reg(regs, params, lambda x: x+1)


def tpl(regs, params):
    apply_f_to_reg(regs, params, lambda x: x*3)


def hlf(regs, params):
    apply_f_to_reg(regs, params, lambda x: x/2)


def jmp_if_condition(regs, params, condition):
    r, offset = params
    if condition(regs.get_register(r)):
        regs.jmp(offset)


def jio(regs, params):
    jmp_if_condition(regs, params, lambda x: x == 1)


def jie(regs, params):
    jmp_if_condition(regs, params, lambda x: x % 2 == 0)


def jmp(regs,params):
    regs.jmp(params[0])


def exec_program(program, registers, trace=False):
    while registers.pc < len(program):
        line = program[registers.pc]
        instruction = line[:3]
        params = line[4:].split(", ")
        if trace:
            print instruction, params
        registers.pc += 1
        globals()[instruction](registers, params)
        if trace:
            print registers

    print "Program complete:", registers


def main(program):
    registers = Registers()
    exec_program(program, registers)

    registers = Registers()
    registers.a = 1
    exec_program(program, registers)



with open("day23.txt", "r") as f:
    lines = map(lambda x:x.rstrip(), f.readlines())

main(lines)