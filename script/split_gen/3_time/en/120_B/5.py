def gcd(a, b):
    while b:
        a, b = b, a%b
    return a
a, b, k = map(int, input().split())
c = gcd(a, b)
d = []
for i in range(1, c+1):
    if c%i == 0:
        d.append(i)
print(d[-k])
