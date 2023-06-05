def gcd(a, b):
    while b:
        a, b = b, a%b
    return a
n, x = map(int, input().split())
a = list(map(int, input().split()))
a.append(x)
a.sort()
d = [a[i+1]-a[i] for i in range(n)]
ans = d[0]
for i in range(1, n):
    ans = gcd(ans, d[i])
print(ans)
