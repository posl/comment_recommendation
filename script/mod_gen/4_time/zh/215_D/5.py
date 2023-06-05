def gcd(a,b):
    if b==0:
        return a
    else:
        return gcd(b,a%b)
    
n,m=map(int,input().split())
a=list(map(int,input().split()))
ans=[0]*(m+1)
for i in range(n):
    for j in range(1,m+1):
        if gcd(a[i],j)==1:
            ans[j]=1
print(sum(ans))
for i in range(1,m+1):
    if ans[i]:
        print(i)

if __name__ == '__main__':
    gcd()