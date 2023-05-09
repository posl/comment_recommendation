def gcd(a, b):
    while b:
        a, b = b, a % b
    return a
N = int(input())
A = list(map(int,input().split()))
L = [0]*N
R = [0]*N
L[0] = A[0]
R[-1] = A[-1]
for i in range(1,N):
    L[i] = gcd(L[i-1],A[i])
for i in range(N-2,-1,-1):
    R[i] = gcd(R[i+1],A[i])
ans = 1
for i in range(N):
    if i == 0:
        ans = max(ans,R[i+1])
    elif i == N-1:
        ans = max(ans,L[i-1])
    else:
        ans = max(ans,gcd(L[i-1],R[i+1]))
print(ans)

if __name__ == '__main__':
    gcd()