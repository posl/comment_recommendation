def gcd(a,b):
    if a%b == 0:
        return b
    else:
        return gcd(b,a%b)
n = int(input())
a = list(map(int,input().split()))
max_gcd = 0
for i in range(2,1001):
    gcdness = 0
    for j in range(n):
        if a[j]%i == 0:
            gcdness += 1
    if gcdness > max_gcd:
        max_gcd = gcdness
        ans = i
print(ans)
