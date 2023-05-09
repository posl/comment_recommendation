def solve():
    N, T = map(int, input().split())
    A = list(map(int, input().split()))
    S = sum(A)
    T -= 1
    print((T // S + 1) % N + 1, T % S + 1)
solve()
