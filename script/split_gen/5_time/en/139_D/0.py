def solve(N: int):
    ans = 0
    for i in range(1, N+1):
        ans += i - 1
    return ans
