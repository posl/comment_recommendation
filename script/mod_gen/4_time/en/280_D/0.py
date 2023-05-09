def factorize(n):
    fct = []
    b, e = 2, 0
    while b * b <= n:
        while n % b == 0:
            n = n // b
            e = e + 1
        if e > 0:
            fct.append((b, e))
        b, e = b + 1, 0
    if n > 1:
        fct.append((n, 1))
    return fct
K = int(input())
factors = factorize(K)
print(factors)
ans = 0
for i in range(len(factors)):
    ans += factors[i][1]
print(ans)

if __name__ == '__main__':
    factorize()