def gcd(a, b):
    while b:
        a, b = b, a % b
    return a
A, B = map(int, input().split())
g = gcd(A, B)
ans = 1
for i in range(2, int(g ** 0.5) + 1):
    if g % i == 0:
        ans += 1
        while g % i == 0:
            g //= i
