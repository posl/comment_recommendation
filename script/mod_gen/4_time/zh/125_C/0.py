def gcd(a,b):
    if b == 0:
        return a
    else:
        return gcd(b,a%b)
n = int(input())
a = list(map(int,input().split()))
l = [0] * n
r = [0] * n
l[0] = a[0]
r[n-1] = a[n-1]
for i in range(1,n):
    l[i] = gcd(l[i-1],a[i])
    r[n-i-1] = gcd(r[n-i],a[n-i-1])
ans = 0
for i in range(n):
    if i == 0:
        ans = max(ans,r[i+1])
    elif i == n-1:
        ans = max(ans,l[i-1])
    else:
        ans = max(ans,gcd(l[i-1],r[i+1]))
print(ans)

if __name__ == '__main__':
    gcd()