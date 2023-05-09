def solve():
    N, X = map(int, input().split())
    if N == 0:
        return 0
    if X == 1:
        return 0
    if X == 2 * N + 3:
        return 2 ** N - 1
    if X <= 2 * N + 1:
        return solve(N - 1, X - 1)
    return solve(N - 1, X - 2 - 2 * N) + 2 ** (N - 1)
