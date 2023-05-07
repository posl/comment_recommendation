def gcd(a,b):
    if b==0:
        return a
    return gcd(b,a%b)
n=int(input())
a=[int(i) for i in input().split()]
ans=0
for i in range(2,1001):
    cnt=0
    for j in range(n):
        if a[j]%i==0:
            cnt+=1
    if cnt>ans:
        ans=cnt
        ansnum=i
print(ansnum)
