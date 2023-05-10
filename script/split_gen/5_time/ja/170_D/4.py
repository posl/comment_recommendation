def gcd(a,b):
    if a % b == 0:
        return(b)
    else:
        return(gcd(b,a%b))
n = int(input())
a = list(map(int,input().split()))
a.sort()
a.reverse()
l = [0]*n
r = [0]*n
l[0] = a[0]
r[n-1] = a[n-1]
for i in range(1,n):
    l[i] = gcd(l[i-1],a[i])
    r[n-1-i] = gcd(r[n-i],a[n-1-i])
ans = 1
for i in range(n):
    if i == 0:
        ans = max(ans,r[1])
    elif i == n-1:
        ans = max(ans,l[n-2])
    else:
        ans = max(ans,gcd(l[i-1],r[i+1]))
print(ans)
