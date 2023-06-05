def gcd(a,b):
    if b==0:
        return a
    else:
        return gcd(b,a%b)
n,x=map(int,input().split())
a=list(map(int,input().split()))
a.append(x)
a.sort()
b=[a[i+1]-a[i] for i in range(n)]
ans=b[0]
for i in range(1,n):
    ans=gcd(ans,b[i])
print(ans)

if __name__ == '__main__':
    gcd()