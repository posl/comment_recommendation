def gcd(a,b):
    if b==0:
        return a
    else:
        return gcd(b,a%b)
N,M=map(int,input().split())
A=list(map(int,input().split()))
A.sort()
maxA=A[-1]
listA=[True]*(maxA+1)
for i in range(N):
    for j in range(A[i],maxA+1,A[i]):
        listA[j]=False
ans=[]
for i in range(1,M+1):
    if listA[i]:
        ans.append(i)
print(len(ans))
for i in ans:
    print(i)
