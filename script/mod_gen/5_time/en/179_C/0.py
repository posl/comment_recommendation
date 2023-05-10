def factors(n):    
    return set(reduce(list.__add__, 
                ([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0)))
N = int(raw_input())
f = sorted(list(factors(N)))
count = 0
for i in f:
    for j in f:
        if N%i == 0 and N%(i*j) == 0:
            count += 1
print count

if __name__ == '__main__':
    factors()