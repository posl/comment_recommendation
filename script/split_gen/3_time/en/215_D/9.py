def gcd(a,b):
    while b!=0:
        a,b=b,a%b
    return a
N,M=map(int,input().split())
A=list(map(int,input().split()))
A.sort()
B=[0]*(M+1)
for i in range(N):
    for j in range(A[i],M+1,A[i]):
        B[j]+=1
ans=0
for i in range(1,M+1):
    if B[i]==1:
        ans+=1
        print(i)
print(ans)
