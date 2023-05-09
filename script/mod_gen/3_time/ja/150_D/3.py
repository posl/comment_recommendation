def gcd(a,b):
    if b==0:
        return a
    else:
        return gcd(b,a%b)
n,m=map(int,input().split())
a=list(map(int,input().split()))
a.sort()
a=list(set(a))
n=len(a)
l=a[0]//2
for i in range(1,n):
    l=l*a[i]//gcd(l,a[i])
ans=0
for i in range(1,m+1):
    if i%l==0:
        ans+=1
print(ans)

if __name__ == '__main__':
    gcd()