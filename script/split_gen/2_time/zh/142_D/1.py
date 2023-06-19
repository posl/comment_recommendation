def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)
a, b = map(int, input().split())
ans = 1
for i in range(2, b+1):
    if b % i == 0:
        if gcd(a, b//i) == 1:
            ans = max(ans, b//i)
print(ans)
