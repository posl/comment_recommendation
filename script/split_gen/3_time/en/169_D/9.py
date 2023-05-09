def prime_factorize(n):
    # 素因数分解
    # 2以上の整数n => [[素因数, 指数], ...]のリスト
    res = []
    for i in range(2, int(n**0.5)+1):
        if n%i != 0:
            continue
        ex = 0
        while n%i == 0:
            ex += 1
            n //= i
        res.append([i, ex])
    if n != 1:
        res.append([n, 1])
    return res
N = int(input())
ans = 0
for p, e in prime_factorize(N):
    tmp = 0
    while e >= tmp:
        tmp += 1
        e -= tmp
        ans += 1
print(ans)
