def get_input():
    n, k = map(int, input().split())
    lrs = [tuple(map(int, input().split())) for _ in range(k)]
    return n, k, lrs
