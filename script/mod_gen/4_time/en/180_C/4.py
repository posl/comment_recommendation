def factors(n):
    return set(reduce(list.__add__, 
                ([i, n//i] for i in range(1, int(n**0.5)+1) if n % i == 0)))
n = int(raw_input())
for i in sorted(factors(n)):
    print i

if __name__ == '__main__':
    factors()