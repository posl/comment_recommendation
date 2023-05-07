def prime_factorize(n):
    from collections import defaultdict
    d = defaultdict(int)
    while n % 2 == 0:
        d[2] += 1
        n //= 2
    i = 3
    while i*i <= n:
        while n % i == 0:
            d[i] += 1
            n //= i
        i += 2
    if n != 1:
        d[n] += 1
    return d

if __name__ == '__main__':
    prime_factorize()