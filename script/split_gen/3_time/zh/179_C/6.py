def solve(N):
    ans = 0
    for i in range(1, N):
        ans += (N-1)//i
    return ans
