def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)
A, B = map(int, input().split())
g = gcd(A, B)
ans = 1
for i in range(2, int(g ** 0.5) + 1):
    if g % i == 0:
        ans += 1
        while g % i == 0:
            g //= i
