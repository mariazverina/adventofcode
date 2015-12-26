
# s = "1"

s = "1321131112"

def sayit(s):
    l = 1
    pc = s[0]
    r = ""
    for c in s[1:]:
        if c == pc:
            l += 1
        else:
            r += str(l) + pc
            pc = c
            l = 1
    r += str(l) + pc
    return r

for _ in range(50):
    s = sayit(s)
    # print s

print len(s)


