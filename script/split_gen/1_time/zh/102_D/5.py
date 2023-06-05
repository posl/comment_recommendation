def main():
    N = int(input())
    A = list(map(int,input().split()))
    sumA = sum(A)
    P = 0
    Q = 0
    R = 0
    S = 0
    ans = 1000000000
    for i in range(N):
        P += A[i]
        if P >= sumA/2:
            break
    for j in range(i):
        Q += A[j]
        if Q >= P/2:
            break
    for k in range(j):
        R += A[k]
        if R >= Q/2:
            break
    S = sumA - P
    ans = min(ans,max(P-Q,Q-R,S-R)-min(P-Q,Q-R,S-R))
    P = 0
    Q = 0
    R = 0
    S = 0
    for i in range(N-1,-1,-1):
        P += A[i]
        if P >= sumA/2:
            break
    for j in range(i,N-1):
        Q += A[j]
        if Q >= P/2:
            break
    for k in range(j,N-1):
        R += A[k]
        if R >= Q/2:
            break
    S = sumA - P
    ans = min(ans,max(P-Q,Q-R,S-R)-min(P-Q,Q-R,S-R))
    print(ans)
