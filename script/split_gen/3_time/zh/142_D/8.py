def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a%b)
a, b = map(int, input().split())
g = gcd(a, b)
cnt = 0
for i in range(1, g+1):
    if gcd(a, b) == 1:
        cnt += 1
print(cnt)
