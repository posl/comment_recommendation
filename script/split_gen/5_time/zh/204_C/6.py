def get_input():
    n, m = map(int, input().split())
    ab = []
    for i in range(m):
        a, b = map(int, input().split())
        ab.append((a, b))
    return n, m, ab
