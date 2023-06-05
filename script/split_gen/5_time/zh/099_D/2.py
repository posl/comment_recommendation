def get_input():
    n, c = map(int, input().split())
    d = [list(map(int, input().split())) for _ in range(c)]
    cc = [list(map(int, input().split())) for _ in range(n)]
    return n, c, d, cc
