def solve(N, C):
    MOD = 10**9 + 7
    C.sort()
    ans = 1
    for i, c in enumerate(C):
        ans = ans * max(0, c - i) % MOD
    return ans
