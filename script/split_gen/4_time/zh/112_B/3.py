def input():
    N, T = map(int, input().split())
    ct = [list(map(int, input().split())) for _ in range(N)]
    return N, T, ct
