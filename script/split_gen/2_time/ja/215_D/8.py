def gcd(a,b):
    while b:
        a,b = b,a%b
    return a
N,M = map(int,input().split())
A = list(map(int,input().split()))
L = [True]*(M+1)
for i in A:
    if L[i]:
        for j in range(i,M+1,i):
            L[j] = False
ans = []
for i in range(1,M+1):
    if L[i]:
        ans.append(i)
print(len(ans))
print(*ans,sep="\n")
