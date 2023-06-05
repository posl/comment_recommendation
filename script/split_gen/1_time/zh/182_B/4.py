def gcd(a, b):
    if a<b:
        a,b=b,a
    while b:
        a,b=b,a%b
    return a
n=int(input())
a=list(map(int, input().split()))
max_gcd=0
ans=0
for i in range(2, 1001):
    cnt=0
    for j in range(n):
        if gcd(a[j], i)==i:
            cnt+=1
    if cnt>=max_gcd:
        max_gcd=cnt
        ans=i
print(ans)
