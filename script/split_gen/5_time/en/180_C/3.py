def factors(n):
    return set(reduce(list.__add__,
                ([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0)))
N = int(raw_input())
f = sorted(list(factors(N)))
for i in f:
    print i
