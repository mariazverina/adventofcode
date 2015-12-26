from itertools import count

password =  map(lambda x:ord(x)-ord('a'), 'cqjxjnds')

forbidden = map(lambda x:ord(x)-ord('a'), 'ilo')

def increment(number_list):
    number_list[-1] += 1
    i = -1
    while number_list[i] >= 26:
        number_list[i] -= 26
        i -= 1
        number_list[i] += 1

    return number_list

print password

for _ in range(2):
    while True:
        password = increment(password)
        if any([c in password for c in forbidden]):
            continue
        if len([1 for (a,b,c) in zip(password,password[1:],password[2:]) if a+1 == b and b+1 == c]) == 0:
            continue
        pairs = [n for (a,b,n) in zip(password,password[1:],count()) if a == b]
        if len(pairs) < 2:
            continue
        if pairs[-1] - pairs[0] < 2:
            continue
        break

    next_pass = map(lambda x:chr(x+ord('a')), password)
    print ''.join(next_pass)

