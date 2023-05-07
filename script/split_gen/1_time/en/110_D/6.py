def factorize(n):
    r = []
    for i in range(1, int(n**0.5)+1):
        if n % i == 0:
            r.append(i)
            if i != n // i:
                r.append(n//i)
    return r
N, M = map(int, input().split())
f = factorize(M)
f.sort()
ans = 0
for i in f:
    if i * N > M:
        continue
    ans = max(ans, i)
print(ans)
