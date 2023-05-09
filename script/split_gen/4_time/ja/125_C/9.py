def gcd(a,b):
    if b == 0:
        return a
    else:
        return gcd(b,a%b)
n = int(input())
a = list(map(int,input().split()))
a.sort()
max_gcd = 0
for i in range(n-1):
    max_gcd = gcd(max_gcd,a[i+1]-a[i])
print(max_gcd)
