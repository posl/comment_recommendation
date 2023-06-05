def solve(N, K):
    ans = 0
    for i in range(1, N+1):
        p = 1/N
        while i < K:
            i *= 2
            p /= 2
        ans += p
    return ans

if __name__ == '__main__':
    solve()