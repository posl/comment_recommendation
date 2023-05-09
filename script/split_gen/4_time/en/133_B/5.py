def get_input():
    n, d = map(int, input().split())
    xs = [list(map(int, input().split())) for _ in range(n)]
    return n, d, xs
