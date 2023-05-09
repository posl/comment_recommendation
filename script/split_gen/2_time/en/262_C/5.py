def solve(N, A):
    ans = 0
    for i in range(N):
        if i + 1 == A[i]:
            ans += 1
    return ans
