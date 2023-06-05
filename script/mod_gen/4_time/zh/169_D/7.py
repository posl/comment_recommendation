def factorize(n):
    res = []
    if n == 1:
        return res
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            res.append(i)
            while n % i == 0:
                n //= i
    if n != 1:
        res.append(n)
    return res
n = int(input())
factors = factorize(n)
ans = 0
for p in factors:
    e = 0
    x = n
    while x % p == 0:
        x //= p
        e += 1
    ans = max(ans, e)
print(ans)

if __name__ == '__main__':
    factorize()