def gcd(x, y):
    if y == 0:
        return x
    else:
        return gcd(y, x % y)
a, b = map(int, input().split())
c = gcd(a, b)
ans = 1
i = 2
while i * i <= c:
    if c % i == 0:
        ans += 1
        while c % i == 0:
            c //= i
    i += 1
