def solve(N, K):
    if K == 1:
        return 0
    if N >= K:
        return (N - K + 1) / N
    return (N - K + 1) / N + (K - 1) / N * (K - 1) / N * solve(N, K - 1)

if __name__ == '__main__':
    solve()