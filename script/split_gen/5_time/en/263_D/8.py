def solve(N, L, R, A):
    # Write your code here
    ans = 0
    for i in range(N):
        ans += A[i]
    ans = min(ans, L*N)
    ans = max(ans, R*N)
    return ans
