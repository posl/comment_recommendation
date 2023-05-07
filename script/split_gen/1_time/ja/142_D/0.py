def gcd(a, b):
    if a < b:
        a, b = b, a
    while b != 0:
        a, b = b, a % b
    return a
a, b = map(int, input().split())
g = gcd(a, b)
ans = 0
for i in range(1, int(g**0.5)+1):
    if g % i == 0:
        ans += 2
