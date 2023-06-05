def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)
n, k = map(int, input().split())
ans = 0
for a in range(1, n + 1):
    ans += n // a * ((a * k + 1) // 2)
    if k % 2 == 0:
        ans -= n // a * ((a * k + k // 2) // k)
for a in range(1, n + 1):
    for b in range(a + 1, n + 1):
        if gcd(a, b) == 1:
            ans -= 2 * (n // a) * (n // b)
for a in range(1, n + 1):
    if gcd(a, k) == 1:
        ans -= (n // a) * (n // k)
print(ans)
