

def divisors(n):
    limit = min(int(n**0.5), 51)
    lower = [x for x in range(1,limit) if n % x == 0]
    higher = [n/x for x in lower]
    return lower + higher

print divisors(1024)
print sum(divisors(100000))

for i in range(1,3400000):
    if i % 10000 == 0:
        print i
    if sum(divisors(i)) * 11 >= 34000000:
        break

print i


