def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a%b)
a, b = map(int, input().split())
g = gcd(a, b)
ans = 1
i = 2
while i*i <= g:
    if g % i == 0:
        ans += 1
        while g % i == 0:
            g //= i
    i += 1
