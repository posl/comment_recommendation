def solve(N, K):
    ans = 0
    for a in range(1, N+1):
        if a % K == 0:
            ans += N // K
        else:
            if N % K >= a:
                ans += N // K + 1
            else:
                ans += N // K
    return ans

if __name__ == '__main__':
    solve()