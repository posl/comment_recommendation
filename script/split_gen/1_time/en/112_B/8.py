def get_input():
    n, t = map(int, input().split())
    ct = [list(map(int, input().split())) for _ in range(n)]
    return n, t, ct
