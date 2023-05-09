def gcd(a,b):
    if a<b:
        a,b=b,a
    while a%b!=0:
        a,b=b,a%b
    return b
n = int(input())
a = list(map(int,input().split()))
a.sort()
b = [a[0]]
for i in range(1,n):
    b.append(gcd(a[i],b[-1]))
ans = 1
for i in range(n):
    ans = max(ans,gcd(a[i],b[i-1]))
print(ans)
