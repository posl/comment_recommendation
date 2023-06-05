def prime_factorize(n):
    if n == 1:
        return []
    res = []
    for i in range(2, int(n**0.5)+1):
        if n%i == 0:
            ex = 0
            while n%i == 0:
                ex += 1
                n //= i
            res.append([i, ex])
    if n != 1:
        res.append([n, 1])
    return res
