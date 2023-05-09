def solve(N,M,A):
    B = [0 for i in range(N)]
    for i in range(N):
        B[i] = A[i] + (B[i-1] if i > 0 else 0)
    ans = 0
    for i in range(M,N+1):
        ans = max(ans, B[i-1] - (B[i-M-1] if i > M else 0))
    return ans
