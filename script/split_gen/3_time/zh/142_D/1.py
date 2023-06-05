def gcd(a, b):
    if a < b:
        a, b = b, a
    while b:
        a, b = b, a%b
    return a
a, b = map(int, input().split())
g = gcd(a, b)
cnt = 1
for i in range(2, int(g**0.5)+1):
    if g % i == 0:
        cnt += 1
        while g % i == 0:
            g //= i
