def solve():
    N, X = map(int, input().split())
    if N == 0:
        print(1 if X > 0 else 0)
        return
    if X <= 2 ** (N + 1) - 1:
        solve(N - 1, X - 1)
    else:
        print(2 ** N + solve(N - 1, X - 2 ** (N + 1) + 1))
    return
