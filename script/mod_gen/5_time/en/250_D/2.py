def prime_factorization(n):
    d = {}
    i = 2
    while i * i <= n:
        while n % i == 0:
            if i in d:
                d[i] += 1
            else:
                d[i] = 1
            n //= i
        i += 1
    if n > 1:
        d[n] = 1
    return d
N = int(input())
ans = 0
for i in range(1, int(N ** (1/3)) + 1):
    if N % i == 0:
        d = prime_factorization(i)
        if len(d) == 1:
            p = list(d.keys())[0]
            if p < N // i ** 3:
                ans += 1
        elif len(d) == 2:
            p = list(d.keys())[0]
            q = list(d.keys())[1]
            if p < q and q ** 3 < N // i ** 3:
                ans += 1
        d = prime_factorization(N // i)
        if len(d) == 1:
            p = list(d.keys())[0]
            if p < i ** 3:
                ans += 1
        elif len(d) == 2:
            p = list(d.keys())[0]
            q = list(d.keys())[1]
            if p < q and q ** 3 < i ** 3:
                ans += 1
print(ans)

if __name__ == '__main__':
    prime_factorization()