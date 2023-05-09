def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)
n,x = map(int, input().split())
xl = list(map(int, input().split()))
xl.append(x)
xl.sort()
gcdl = []
for i in range(n):
    gcdl.append(xl[i+1] - xl[i])
ans = gcdl[0]
for i in range(1,n):
    ans = gcd(ans, gcdl[i])
print(ans)
