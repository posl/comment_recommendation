def get_input():
    n, m = map(int, input().split())
    edges = [list(map(int, input().split())) for _ in range(m)]
    return n, m, edges
