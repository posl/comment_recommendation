def gcd(a, b):
    if a < b:
        a, b = b, a
    if b == 0:
        return a
    else:
        return gcd(b, a % b)
k = int(input())
ans = 0
for a in range(1, k + 1):
    for b in range(1, k + 1):
        for c in range(1, k + 1):
            g = gcd(a, b)
            ans += gcd(g, c)
print(ans)
