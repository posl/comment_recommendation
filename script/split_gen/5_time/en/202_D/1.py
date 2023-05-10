def ncr(n,r):
    if n<r:
        return 0
    if r==0:
        return 1
    if r==1:
        return n
    if r>n//2:
        return ncr(n,n-r)
    return ncr(n-1,r-1)+ncr(n-1,r)
a,b,k=map(int,input().split())
ans=""
for i in range(a+b):
    if a==0:
        ans+="b"
        b-=1
        continue
    if b==0:
        ans+="a"
        a-=1
        continue
    if k<=ncr(a+b-1,b):
        ans+="a"
        a-=1
    else:
        ans+="b"
        k-=ncr(a+b-1,b)
        b-=1
print(ans)
