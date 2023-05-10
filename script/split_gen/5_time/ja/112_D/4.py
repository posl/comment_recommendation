def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a
n, m = map(int, input().split())
m //= n
ans = 1
for i in range(1, int(m ** 0.5) + 1):
    if m % i == 0:
        ans = max(ans, i)
        ans = max(ans, m // i)
print(ans)
