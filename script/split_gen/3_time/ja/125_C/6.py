def gcd(a,b):
    if a%b == 0:
        return b
    else:
        return gcd(b,a%b)
N = int(input())
A = list(map(int,input().split()))
L = [0] * (N+1)
R = [0] * (N+1)
L[0] = A[0]
R[N-1] = A[N-1]
for i in range(1,N):
    L[i] = gcd(L[i-1],A[i])
    R[N-i-1] = gcd(R[N-i],A[N-i-1])
ans = 0
for i in range(N):
    if i == 0:
        ans = max(ans,R[i+1])
    elif i == N-1:
        ans = max(ans,L[i-1])
    else:
        ans = max(ans,gcd(L[i-1],R[i+1]))
print(ans)
