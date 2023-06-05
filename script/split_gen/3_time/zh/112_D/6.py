def gcd(a, b):
    while b:
        a, b = b, a % b
    return a
n, m = map(int, input().split())
#n, m = 100000, 1000000000
g = gcd(m, n)
m = m // g
n = n // g
ans = 1
i = 2
while i * i <= m:
    if m % i == 0:
        ans = max(ans, i)
        while m % i == 0:
            m //= i
    i += 1
