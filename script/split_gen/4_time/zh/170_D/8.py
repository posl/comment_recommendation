def gcd(a, b):
    while b:
        a, b = b, a % b
    return a
n = int(input())
a = list(map(int, input().split()))
g = [0] * (n + 1)
for i in range(n - 1, -1, -1):
    g[i] = gcd(a[i], g[i + 1])
ans = 0
for i in range(n):
    if (a[i] == g[i + 1]):
        ans += 1
print(ans)
