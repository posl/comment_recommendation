def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)
n,m = map(int, input().split())
for i in range(1, int(m/n)+1):
    if m % i == 0:
        if i * n <= m:
            ans = i
print(ans)
