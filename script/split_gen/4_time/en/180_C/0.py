def factors(n):    
    return set(reduce(list.__add__, 
                ([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0)))
n = int(raw_input().strip())
f = factors(n)
for i in sorted(f):
    print i
