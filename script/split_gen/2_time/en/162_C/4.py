def gcd(a, b):
    return a if b == 0 else gcd(b, a % b)
k = int(input())
ans = 0
for i in range(1, k + 1):
    for j in range(1, k + 1):
        for l in range(1, k + 1):
            ans += gcd(gcd(i, j), l)
print(ans)
