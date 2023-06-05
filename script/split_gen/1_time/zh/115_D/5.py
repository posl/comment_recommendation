def solve():
    N, X = map(int, input().split())
    if X == 1:
        print(0)
        return
    if X == 2**(N+1) - 1:
        print(2**N - 1)
        return
    if X < 2**(N+1) - 1:
        solve()
    else:
        print(2**N - 1)
        return
solve()
