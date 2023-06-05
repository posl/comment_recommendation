def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)
n = int(input())
a = list(map(int, input().split()))
cnt = 0
d = {}
for i in range(n):
    for j in range(i + 1, n):
        g = gcd(a[i], a[j])
        if g == 1:
            continue
        if g in d:
            d[g] += 1
        else:
            d[g] = 1
        if a[i] // g in d:
            cnt += d[a[i] // g]
print(cnt)
